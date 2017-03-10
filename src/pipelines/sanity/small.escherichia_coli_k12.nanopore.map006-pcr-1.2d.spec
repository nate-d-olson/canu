gridOptions=-q big.q

genomeSize=4.8m
stopOnReadQuality=false

#
#  -- In gatekeeper store 'correction/small.escherichia_coli_k12.nanopore.map006-pcr-1.2d.gkpStore':
#  --   Found 20365 reads.
#  --   Found 140042151 bases (29.17 times coverage).
#  --
#  --   Read length histogram (one '*' equals 41.48 reads):
#  --        0    999      0 
#  --     1000   1999    706 *****************
#  --     2000   2999   1682 ****************************************
#  --     3000   3999   1624 ***************************************
#  --     4000   4999   1543 *************************************
#  --     5000   5999   1905 *********************************************
#  --     6000   6999   2691 ****************************************************************
#  --     7000   7999   2904 **********************************************************************
#  --     8000   8999   2609 **************************************************************
#  --     9000   9999   1946 **********************************************
#  --    10000  10999   1280 ******************************
#  --    11000  11999    733 *****************
#  --    12000  12999    397 *********
#  --    13000  13999    181 ****
#  --    14000  14999    109 **
#  --    15000  15999     38 
#  --    16000  16999      9 
#  --    17000  17999      4 
#  --    18000  18999      2 
#  --    19000  19999      0 
#  --    20000  20999      0 
#  --    21000  21999      0 
#  --    22000  22999      1 
#  --    23000  23999      0 
#  --    24000  24999      0 
#  --    25000  25999      1 
#

-nanopore-raw /data/regression/reads/escherichia_coli_k12.nanopore.map006-pcr-1.2d.fasta.xz

onSuccess=/work/canu/src/pipelines/sanity/success.escherichia_coli_k12.sh

