import sys

bitmap = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message')
print('Enter the message to display with the bitmap')

message = input('> ')
if message == '':
    sys.exit()

### Personal Solution
# aux = len(message)
# j = 0
# new_bitmap = []
# for line in bitmap.splitlines():
#     new_line = ''
#     for i in line:
#         if i != ' ':
#             new_line = new_line + message[j]
#             j += 1
#         else:
#             new_line = new_line + ' '
#             j += 1
#         if j == len(message):
#             j = 0
#     j = 0
#     new_bitmap.append(new_line)
#
# print('\n'.join(new_bitmap))

### Book's solution
# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # new line
