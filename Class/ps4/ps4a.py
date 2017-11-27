# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) <= 1:
        result = [sequence]
    else:
        char = sequence[0]
        perms = get_permutations(sequence[1:])
        result = []
        for perm in perms:
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])

    return result


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'asd123'
    print('Input', example_input)
    print('Expected Output:', ['123ads','123asd','123das','123dsa','123sad','123sda','12a3ds','12a3sd','12ad3s','12ads3','12as3d','12asd3','12d3as','12d3sa','12da3s','12das3','12ds3a','12dsa3','12s3ad','12s3da','12sa3d','12sad3','12sd3a','12sda3','132ads','132asd','132das','132dsa','132sad','132sda','13a2ds','13a2sd','13ad2s','13ads2','13as2d','13asd2','13d2as','13d2sa','13da2s','13das2','13ds2a','13dsa2','13s2ad','13s2da','13sa2d','13sad2','13sd2a','13sda2','1a23ds','1a23sd','1a2d3s','1a2ds3','1a2s3d','1a2sd3','1a32ds','1a32sd','1a3d2s','1a3ds2','1a3s2d','1a3sd2','1ad23s','1ad2s3','1ad32s','1ad3s2','1ads23','1ads32','1as23d','1as2d3','1as32d','1as3d2','1asd23','1asd32','1d23as','1d23sa','1d2a3s','1d2as3','1d2s3a','1d2sa3','1d32as','1d32sa','1d3a2s','1d3as2','1d3s2a','1d3sa2','1da23s','1da2s3','1da32s','1da3s2','1das23','1das32','1ds23a','1ds2a3','1ds32a','1ds3a2','1dsa23','1dsa32','1s23ad','1s23da','1s2a3d','1s2ad3','1s2d3a','1s2da3','1s32ad','1s32da','1s3a2d','1s3ad2','1s3d2a','1s3da2','1sa23d','1sa2d3','1sa32d','1sa3d2','1sad23','1sad32','1sd23a','1sd2a3','1sd32a','1sd3a2','1sda23','1sda32','213ads','213asd','213das','213dsa','213sad','213sda','21a3ds','21a3sd','21ad3s','21ads3','21as3d','21asd3','21d3as','21d3sa','21da3s','21das3','21ds3a','21dsa3','21s3ad','21s3da','21sa3d','21sad3','21sd3a','21sda3','231ads','231asd','231das','231dsa','231sad','231sda','23a1ds','23a1sd','23ad1s','23ads1','23as1d','23asd1','23d1as','23d1sa','23da1s','23das1','23ds1a','23dsa1','23s1ad','23s1da','23sa1d','23sad1','23sd1a','23sda1','2a13ds','2a13sd','2a1d3s','2a1ds3','2a1s3d','2a1sd3','2a31ds','2a31sd','2a3d1s','2a3ds1','2a3s1d','2a3sd1','2ad13s','2ad1s3','2ad31s','2ad3s1','2ads13','2ads31','2as13d','2as1d3','2as31d','2as3d1','2asd13','2asd31','2d13as','2d13sa','2d1a3s','2d1as3','2d1s3a','2d1sa3','2d31as','2d31sa','2d3a1s','2d3as1','2d3s1a','2d3sa1','2da13s','2da1s3','2da31s','2da3s1','2das13','2das31','2ds13a','2ds1a3','2ds31a','2ds3a1','2dsa13','2dsa31','2s13ad','2s13da','2s1a3d','2s1ad3','2s1d3a','2s1da3','2s31ad','2s31da','2s3a1d','2s3ad1','2s3d1a','2s3da1','2sa13d','2sa1d3','2sa31d','2sa3d1','2sad13','2sad31','2sd13a','2sd1a3','2sd31a','2sd3a1','2sda13','2sda31','312ads','312asd','312das','312dsa','312sad','312sda','31a2ds','31a2sd','31ad2s','31ads2','31as2d','31asd2','31d2as','31d2sa','31da2s','31das2','31ds2a','31dsa2','31s2ad','31s2da','31sa2d','31sad2','31sd2a','31sda2','321ads','321asd','321das','321dsa','321sad','321sda','32a1ds','32a1sd','32ad1s','32ads1','32as1d','32asd1','32d1as','32d1sa','32da1s','32das1','32ds1a','32dsa1','32s1ad','32s1da','32sa1d','32sad1','32sd1a','32sda1','3a12ds','3a12sd','3a1d2s','3a1ds2','3a1s2d','3a1sd2','3a21ds','3a21sd','3a2d1s','3a2ds1','3a2s1d','3a2sd1','3ad12s','3ad1s2','3ad21s','3ad2s1','3ads12','3ads21','3as12d','3as1d2','3as21d','3as2d1','3asd12','3asd21','3d12as','3d12sa','3d1a2s','3d1as2','3d1s2a','3d1sa2','3d21as','3d21sa','3d2a1s','3d2as1','3d2s1a','3d2sa1','3da12s','3da1s2','3da21s','3da2s1','3das12','3das21','3ds12a','3ds1a2','3ds21a','3ds2a1','3dsa12','3dsa21','3s12ad','3s12da','3s1a2d','3s1ad2','3s1d2a','3s1da2','3s21ad','3s21da','3s2a1d','3s2ad1','3s2d1a','3s2da1','3sa12d','3sa1d2','3sa21d','3sa2d1','3sad12','3sad21','3sd12a','3sd1a2','3sd21a','3sd2a1','3sda12','3sda21','a123ds','a123sd','a12d3s','a12ds3','a12s3d','a12sd3','a132ds','a132sd','a13d2s','a13ds2','a13s2d','a13sd2','a1d23s','a1d2s3','a1d32s','a1d3s2','a1ds23','a1ds32','a1s23d','a1s2d3','a1s32d','a1s3d2','a1sd23','a1sd32','a213ds','a213sd','a21d3s','a21ds3','a21s3d','a21sd3','a231ds','a231sd','a23d1s','a23ds1','a23s1d','a23sd1','a2d13s','a2d1s3','a2d31s','a2d3s1','a2ds13','a2ds31','a2s13d','a2s1d3','a2s31d','a2s3d1','a2sd13','a2sd31','a312ds','a312sd','a31d2s','a31ds2','a31s2d','a31sd2','a321ds','a321sd','a32d1s','a32ds1','a32s1d','a32sd1','a3d12s','a3d1s2','a3d21s','a3d2s1','a3ds12','a3ds21','a3s12d','a3s1d2','a3s21d','a3s2d1','a3sd12','a3sd21','ad123s','ad12s3','ad132s','ad13s2','ad1s23','ad1s32','ad213s','ad21s3','ad231s','ad23s1','ad2s13','ad2s31','ad312s','ad31s2','ad321s','ad32s1','ad3s12','ad3s21','ads123','ads132','ads213','ads231','ads312','ads321','as123d','as12d3','as132d','as13d2','as1d23','as1d32','as213d','as21d3','as231d','as23d1','as2d13','as2d31','as312d','as31d2','as321d','as32d1','as3d12','as3d21','asd123','asd132','asd213','asd231','asd312','asd321','d123as','d123sa','d12a3s','d12as3','d12s3a','d12sa3','d132as','d132sa','d13a2s','d13as2','d13s2a','d13sa2','d1a23s','d1a2s3','d1a32s','d1a3s2','d1as23','d1as32','d1s23a','d1s2a3','d1s32a','d1s3a2','d1sa23','d1sa32','d213as','d213sa','d21a3s','d21as3','d21s3a','d21sa3','d231as','d231sa','d23a1s','d23as1','d23s1a','d23sa1','d2a13s','d2a1s3','d2a31s','d2a3s1','d2as13','d2as31','d2s13a','d2s1a3','d2s31a','d2s3a1','d2sa13','d2sa31','d312as','d312sa','d31a2s','d31as2','d31s2a','d31sa2','d321as','d321sa','d32a1s','d32as1','d32s1a','d32sa1','d3a12s','d3a1s2','d3a21s','d3a2s1','d3as12','d3as21','d3s12a','d3s1a2','d3s21a','d3s2a1','d3sa12','d3sa21','da123s','da12s3','da132s','da13s2','da1s23','da1s32','da213s','da21s3','da231s','da23s1','da2s13','da2s31','da312s','da31s2','da321s','da32s1','da3s12','da3s21','das123','das132','das213','das231','das312','das321','ds123a','ds12a3','ds132a','ds13a2','ds1a23','ds1a32','ds213a','ds21a3','ds231a','ds23a1','ds2a13','ds2a31','ds312a','ds31a2','ds321a','ds32a1','ds3a12','ds3a21','dsa123','dsa132','dsa213','dsa231','dsa312','dsa321','s123ad','s123da','s12a3d','s12ad3','s12d3a','s12da3','s132ad','s132da','s13a2d','s13ad2','s13d2a','s13da2','s1a23d','s1a2d3','s1a32d','s1a3d2','s1ad23','s1ad32','s1d23a','s1d2a3','s1d32a','s1d3a2','s1da23','s1da32','s213ad','s213da','s21a3d','s21ad3','s21d3a','s21da3','s231ad','s231da','s23a1d','s23ad1','s23d1a','s23da1','s2a13d','s2a1d3','s2a31d','s2a3d1','s2ad13','s2ad31','s2d13a','s2d1a3','s2d31a','s2d3a1','s2da13','s2da31','s312ad','s312da','s31a2d','s31ad2','s31d2a','s31da2','s321ad','s321da','s32a1d','s32ad1','s32d1a','s32da1','s3a12d','s3a1d2','s3a21d','s3a2d1','s3ad12','s3ad21','s3d12a','s3d1a2','s3d21a','s3d2a1','s3da12','s3da21','sa123d','sa12d3','sa132d','sa13d2','sa1d23','sa1d32','sa213d','sa21d3','sa231d','sa23d1','sa2d13','sa2d31','sa312d','sa31d2','sa321d','sa32d1','sa3d12','sa3d21','sad123','sad132','sad213','sad231','sad312','sad321','sd123a','sd12a3','sd132a','sd13a2','sd1a23','sd1a32','sd213a','sd21a3','sd231a','sd23a1','sd2a13','sd2a31','sd312a','sd31a2','sd321a','sd32a1','sd3a12','sd3a21','sda123','sda132','sda213','sda231','sda312','sda321'])
    print('Actual Output', get_permutations(example_input))