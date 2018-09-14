######################################################################
# Author: Berucha Cintron
# Username: cintronb
#
# Assignment: A08: UPC Bar Codes
#
# Purpose: Learn about an important application of computer science, the UPC code, and work on the design of a larger problem.
#
######################################################################
# Acknowledgements: Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


class Barcode(object):
    def __init__(self, barcode, turt):
        '''
        Initializes for the Barcode class
        :param barcode: the code the user inputted
        :param turt: a turtle object
        '''
        self.left_dict = {0: '0001101',     # the dictionary of binary code for every element of the barcode on the left side
                          1: '0011001',
                          2: '0010011',
                          3: '0111101',
                          4: '0100011',
                          5: '0110001',
                          6: '0101111',
                          7: '0111011',
                          8: '0110111',
                          9: '0001011'}
        self.right_dict = {0: '1110010',    # the dictionary of binary code for every element of the barcode on the right side
                           1: '1100110',
                           2: '1101100',
                           3: '1000010',
                           4: '1011100',
                           5: '1001110',
                           6: '1010000',
                           7: '1000100',
                           8: '1001000',
                           9: '1110100'}
        self.barcode = barcode  # changing the local variable to a variable that can be used in different instances within the class
        self.num_sys_char = barcode[0]  # the element in the 0 place of the barcode is the number system character
        self.man_id_num = barcode[1:6]  # the elements in the in the 1st to fifth places of the barcode are the manufacturer ID number
        self.item_num = barcode[6:11]  # the elements in the sixth to tenth places of the barcode are the item number
        self.mod_chk_char = barcode[-1]  # the element in the last place of the barcode is the modulo check character
        self.lft_grd_brs_pat = '101'  # the left hand guard bars pattern is black, white, black
        self.tall_cntr_brs_pat = '01010'  # the tall center bars pattern is white, black, white, black, white
        self.rit_grd_brs_pat = self.lft_grd_brs_pat  # the right hand guard bars pattern is the same as the left
        self.turt = turt  # changing the local variable to a variable that can be used in different instances within the class
        self.turt.ht()  # hides the turtle
        self.turt.seth(270)  # sets the height of the turtle
        self.turt.pensize(3)  # sets the pen size of the turtle
        self.turt.speed(0)  # determines how fast the turtle goes
        self.x = 0  # sets the position on the x axis
        self.y = 0  # sets the position on the y axis
        self.turt.goto(self.x, self.y)  # tells the turtle where to go
        self.concatenate()  # calls the function
        self.draw_barcode()  # calls the function
        self.draw_numbers()  # calls the function

    def concatenate(self):
        '''
        Concatenates all the binary code for every element of the barcode into a single binary barcode strand
        :return: None
        '''
        bin_nsc = self.left_dict[int(self.num_sys_char)]  # assigns the binary code to the number system character
        bin_min = ''
        for element in self.man_id_num:  # assigns the binary code to each element
            bin_min += self.left_dict[int(element)]
        bin_itnm = ''
        for ele in self.item_num:  # assigns the binary code to each element
            bin_itnm += self.right_dict[int(ele)]
        bin_mcc = self.right_dict[int(self.mod_chk_char)]  # assigns the binary code to the modulo check character

        # puts all the binary code for every element in the barcode to make up the entire binary barcode
        self.bin_barcode = self.lft_grd_brs_pat + bin_nsc + bin_min + \
                           self.tall_cntr_brs_pat + bin_itnm + bin_mcc + self.rit_grd_brs_pat

    def draw_barcode(self):
        '''
        Determines the length and color of the bars of the barcode and draws them
        :return: None
        '''
        for i in range(len(self.bin_barcode)):
            if (i >= 0 and i < 10) or (i >= 45 and i < 51) or (i >= 85):  # the bars within these parameters must be longer than the rest of the barcode
                if self.bin_barcode[i] == '1':  # the ones in the binary code are black
                    self.turt.color('black')
                else:
                    self.turt.color('white')  # the zeros in the binary code are white
                self.turt.pendown()
                self.turt.goto(self.x, self.y + -180)
                self.turt.penup()
                self.turt.goto(self.x + 3, self.y)
                self.x += 3
            else:
                if self.bin_barcode[i] == '1':  # the ones in the binary code are black
                    self.turt.color('black')
                else:
                    self.turt.color('white')  # the zeros in the binary code are white
                self.turt.pendown()
                self.turt.goto(self.x, self.y + -165)
                self.turt.penup()
                self.turt.goto(self.x + 3, self.y)
                self.x += 3

    def draw_numbers(self):
        '''
        Prints the numbers in the barcode in specific positions and formatting
        :return: None
        '''
        for i in range(len(self.barcode)):
            if i == 0:  # the number system character is in the 0 place and it must be outside of the barcode
                self.turt.goto(-25, -200)
                self.turt.write(self.barcode[i], font=('Arial', 24, 'normal'))
            if i == 11:  # the modulo check character is in the 11 place and it must be outside of the barcode
                self.turt.goto(290, -200)
                self.turt.write(self.barcode[i], font=('Arial', 24, 'normal'))
        self.x = 34
        for i in range(len(self.barcode)):
            if i in [1, 2, 3, 4, 5]:  # the manufacturer ID numbers must be under the barcode on the left side
                self.turt.goto(self.x, -200)
                self.turt.write(self.barcode[i], font=('Arial', 24, 'normal'))
                self.x += 20
        self.x = 156
        for i in range(len(self.barcode)):
            if i in [6, 7, 8, 9, 10]:  # the item numbers must be under the barcode on the right side
                self.turt.goto(self.x, -200)
                self.turt.write(self.barcode[i], font=('Arial', 24, 'normal'))
                self.x += 20


def is_valid_input(barcode):
    '''
    Evaluates whether the inputted code follows the requirements of being only 12 integers
    :param barcode: the code the user inputs
    :return: True or False
    '''
    for element in barcode:  # checks every element of the inputted code
        if not str.isdigit(element):  # checks if the code entered is only numbers
            return False  # if it isn't then it is not a valid input
    else:
        if len(barcode) == 12:  # checks if the barcide is the right length
            return True
        return False


def is_valid_modulo(barcode):
    '''
    Checks if the barcode has a valid modulo check digit
    :param barcode: the code the user inputs
    :return: True or False
    '''
    even_sum = 0
    odd_sum = 0
    barcode = list(barcode)
    modulo_check_digit = barcode.pop(-1)
    for i in range(0, len(barcode), 2):  # takes every odd number placement and adds them all together to get odd_sum
        odd_sum += int(barcode[i])

    odd_total = odd_sum * 3
    for j in range(1, len(barcode), 2):  # takes every even number placement and adds them all together to get even_sum
        even_sum += int(barcode[j])
    digit_total = odd_total + even_sum
    total_remainder = digit_total % 10
    if total_remainder != 0:
        check_digit = 10 - total_remainder
        return int(modulo_check_digit) == check_digit  # returns true or false
    else:
        return total_remainder == int(modulo_check_digit)  # returns true or false


def main():
    '''
    Runs the progam
    :return: None
    '''
    window = turtle.Screen()
    turt = turtle.Turtle()

    barcode = input("Enter a 12 digit code [0-9]: ")
    while not is_valid_input(barcode):
        barcode = input("Invalid number. Enter a 12 digit code [0-9]: ")

    if is_valid_modulo(barcode):
        barcode = Barcode(barcode, turt)

    else:
        turt.ht()
        turt.color("red")
        turt.setpos(-300, 0)
        turt.write('Your code is not a valid UPC barcode.\n'
                   'To be able to draw a barcode, please try \n'
                   'again and try to enter a valid UPC 12 digit code.', font=("Arial", 20, 'normal'))

    window.exitonclick()


if __name__ == "__main__":
    main()
