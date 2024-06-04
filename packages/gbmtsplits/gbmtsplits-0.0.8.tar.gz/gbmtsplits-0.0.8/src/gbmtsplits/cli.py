import os
import argparse
import pandas as pd
from timeit import default_timer as timer
from .logs.config import enable_file_logger
from .split import GloballyBalancedSplit
from .clustering import RandomClustering, LeaderPickerClustering, MaxMinClustering, MurckoScaffoldClustering

def main():

    # Parse command line arguments ###############################
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Input file with the data in a pivoted csv/tsv format. \
                            A column with the SMILES must be provided and each target must be in a separate column.')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Output file with the data with additional columns \
                            the assigned subset (and Minimum interset Tanimoto distance).')
    parser.add_argument('-sc','--smiles_column', type=str, default='SMILES',
                        help='Name of the column with the SMILES')
    parser.add_argument('-tc','--target_columns', type=str, nargs='+', default=None,
                        help="Name of the columns with the targets. If not provided, \
                            all columns except the SMILES and --ignore_columns' columns will be used")
    parser.add_argument('-ic','--ignore_columns', type=str, nargs='+', default=None,
                        help='Name of the columns to ignore')
    parser.add_argument('-ns', '--n_splits', type=int, default=1,
                         help='Number of splits to generate')
    parser.add_argument('-c','--clustering', type=str, default='dissimilarity_leader',
                        help='Clustering algorithm to use. \
                            Options: random, dissimilarity_leader, dissimilarity_maxmin or murcko')
    parser.add_argument('-nc','--n_clusters', type=int, default=None,
                        help='Number of clusters to use. Only used for random clustering. \
                            If None, the number of clusters is equal to the number of molecules divided by 100')
    parser.add_argument('-rs','--random_seed', type=int, default=42,
                        help='Seed for the random clustering')
    parser.add_argument('-ct','--cluster_threshold', type=float, default=0.7,
                        help='Minimum distance between cluster centers. Only used for dissimilarity clustering.')
    parser.add_argument('-s', '--sizes', type=float, nargs='+', default=[0.8, 0.1, 0.1],
                        help='Sizes of the subsets')
    parser.add_argument('-t','--time_limit', type=int, default=60,
                        help='Time limit for linear combination of clusters in seconds')
    parser.add_argument('-mtd', '--min_Tanimoto_distance', action='store_true',
                        help='Compute the minimum Tanimoto distance between a molecule in a subset and the molecules in the other subsets')
    
    # Start the timer
    start_time = timer()
    
    # Parse arguments 
    args = parser.parse_args()
    # Read input data from csv/tsv file ##########################
    if '.csv' in args.input:
        df = pd.read_csv(args.input)
    elif '.tsv' in args.input:
        df = pd.read_csv(args.input, sep='\t')
    else:
        raise ValueError('Input file must be a csv or tsv file')
    
    if args.target_columns is None and args.ignore_columns is None:
        args.target_columns = [col for col in df.columns if col != args.smiles_column]
    elif args.target_columns is None and args.ignore_columns is not None:
        args.target_columns = [col for col in df.columns if col != args.smiles_column and col not in args.ignore_columns]

    if not args.output:
        args.output = args.input.split('.')[0] 

    # Enable logging #############################################
    logSettings = enable_file_logger(
        os.path.dirname(args.output),
        "gbmtsplits.log",
        False,
        __name__,
        vars(args),
        disable_existing_loggers=False,
    )
    log = logSettings.log
    

    # Setup splitter #############################################
    if args.clustering == 'random':
        clustering = RandomClustering(n_clusters=args.n_clusters, seed=args.random_seed)
        args.output += '_RGBS.'
    elif args.clustering == 'dissimilarity_leader':
        clustering = LeaderPickerClustering(similarity_threshold=args.cluster_threshold)
        args.output += '_LPDGBS.'
    elif args.clustering == 'dissimilarity_maxmin':
        clustering = MaxMinClustering(n_clusters=args.n_clusters, seed=args.random_seed)
        args.output += '_MMDGBS.'
    elif args.clustering == 'murcko':
        clustering = MurckoScaffoldClustering()
        args.output += '_MSGBS.'
    else:
        raise ValueError('Clustering algorithm not recognized')

    splitter = GloballyBalancedSplit(
        sizes = args.sizes,
        clustering_method=clustering,
        time_limit_seconds=args.time_limit,
        min_distance=args.min_Tanimoto_distance,
        n_splits=args.n_splits
        )
    
    # Split data #################################################
    df = splitter(df, targets=args.target_columns, smiles_column=args.smiles_column)

    # Write output ###############################################
    
    # Use same extension  and compression as input file
    args.output += '.'.join(args.input.split('.')[1:])

    if '.csv' in args.output:
        df.to_csv(args.output, index=False)
    elif '.tsv' in args.output:
        df.to_csv(args.output, sep='\t', index=False)
    
    # Print elapsed time #########################################
    elapsed_time = timer() - start_time
    log.info('Elapsed time: {:.2f} seconds'.format(elapsed_time))
        
if __name__ == '__main__':

    main()