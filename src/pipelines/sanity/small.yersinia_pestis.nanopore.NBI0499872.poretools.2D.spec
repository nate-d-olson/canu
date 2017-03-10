gridOptions=-q big.q

genomeSize=4.8m
stopOnReadQuality=false

#
#  -- In gatekeeper store 'correction/test.gkpStore':
#  --   Found 99476 reads.
#  --   Found 805194313 bases (167.74 times coverage).
#  --
#  --   Read length histogram (one '*' equals 183.87 reads):
#  --        0    999      0 
#  --     1000   1999   2843 ***************
#  --     2000   2999   3573 *******************
#  --     3000   3999   4820 **************************
#  --     4000   4999   6796 ************************************
#  --     5000   5999   9459 ***************************************************
#  --     6000   6999  11992 *****************************************************************
#  --     7000   7999  12871 **********************************************************************
#  --     8000   8999  11824 ****************************************************************
#  --     9000   9999  10036 ******************************************************
#  --    10000  10999   7539 *****************************************
#  --    11000  11999   5547 ******************************
#  --    12000  12999   3930 *********************
#  --    13000  13999   2649 **************
#  --    14000  14999   1779 *********
#  --    15000  15999   1198 ******
#  --    16000  16999    741 ****
#  --    17000  17999    555 ***
#  --    18000  18999    390 **
#  --    19000  19999    227 *
#  --    20000  20999    191 *
#  --    21000  21999    125 
#  --    22000  22999    104 
#  --    23000  23999     91 
#  --    24000  24999     57 
#  --    25000  25999     33 
#  --    26000  26999     23 
#  --    27000  27999     16 
#  --    28000  28999     13 
#  --    29000  29999     12 
#  --    30000  30999      9 
#  --    31000  31999      7 
#  --    32000  32999      3 
#  --    33000  33999      7 
#  --    34000  34999      2 
#  --    35000  35999      3 
#  --    36000  36999      0 
#  --    37000  37999      2 
#  --    38000  38999      0 
#  --    39000  39999      1 
#  --    40000  40999      3 
#  --    41000  41999      1 
#  --    42000  42999      1 
#  --    43000  43999      0 
#  --    44000  44999      0 
#  --    45000  45999      0 
#  --    46000  46999      0 
#  --    47000  47999      0 
#  --    48000  48999      0 
#  --    49000  49999      1 
#  --    50000  50999      0 
#  --    51000  51999      0 
#  --    52000  52999      0 
#  --    53000  53999      0 
#  --    54000  54999      0 
#  --    55000  55999      0 
#  --    56000  56999      0 
#  --    57000  57999      0 
#  --    58000  58999      0 
#  --    59000  59999      0 
#  --    60000  60999      0 
#  --    61000  61999      1 
#  --    62000  62999      0 
#  --    63000  63999      0 
#  --    64000  64999      0 
#  --    65000  65999      0 
#  --    66000  66999      0 
#  --    67000  67999      0 
#  --    68000  68999      0 
#  --    69000  69999      0 
#  --    70000  70999      0 
#  --    71000  71999      0 
#  --    72000  72999      0 
#  --    73000  73999      0 
#  --    74000  74999      0 
#  --    75000  75999      0 
#  --    76000  76999      0 
#  --    77000  77999      0 
#  --    78000  78999      0 
#  --    79000  79999      1 
#

-nanopore-raw /data/regression/reads/yersinia_pestis.nanopore.NBI0499872.poretools.2D.fasta.xz

onSuccess=/work/canu/src/pipelines/sanity/success.yersinia_pestis_i195.sh

