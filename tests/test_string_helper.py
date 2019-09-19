import unittest
from Source.string_helpers import *


class TestStringHelper(unittest.TestCase):

    def test_line_break_top(self):
        self.assertEqual(line_break(10, True, False), "  ╔══════════╗")

    def test_line_break_middle(self):
        self.assertEqual(line_break(10, False, False), "  ╠══════════╣")

    def test_line_break_bottom(self):
        self.assertEqual(line_break(10, False, True), "  ╚══════════╝")

    def test_line_break_2_top(self):
        self.assertEqual(line_break_2(10, 7, True, False), "  ╔══════════╦═══════╗")

    def test_line_break_2_middle(self):
        self.assertEqual(line_break_2(10, 7, False, False), "  ╠══════════╬═══════╣")

    def test_line_break_2_bottom(self):
        self.assertEqual(line_break_2(10, 7, False, True), "  ╚══════════╩═══════╝")

    def test_line_break_4_top(self):
        self.assertEqual(line_break_4(10, 7, 3, 2, True, False), "  ╔══════════╦═══════╦═══╦══╗")

    def test_line_break_4_middle(self):
        self.assertEqual(line_break_4(10, 7, 3, 2, False, False), "  ╠══════════╬═══════╬═══╬══╣")

    def test_line_break_4_bottom(self):
        self.assertEqual(line_break_4(10, 7, 3, 2, False, True), "  ╚══════════╩═══════╩═══╩══╝")

    def test_update_menu_string_down_to_2(self):
        self.assertMultiLineEqual(update_menu_string(ascii_images["drink_menu_string"], 0, False), """
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         
  ╔═══════════════════════════════╗
  ║ [2]  View Drink Options       ║
  ╚═══════════════════════════════╝

    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    

    [14] Exit                      

                                   

""")

    def test_update_menu_string_down_to_3(self):
        self.assertMultiLineEqual(update_menu_string(update_menu_string(ascii_images["drink_menu_string"], 0, False), 1, False), """
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         

    [2]  View Drink Options        

  ╔═══════════════════════════════╗
  ║ [3]  Add Team Members         ║
  ╚═══════════════════════════════╝
    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    

    [14] Exit                      

                                   

""")

    def test_update_menu_string_up_to_2(self):
        self.assertMultiLineEqual(
            update_menu_string(update_menu_string(update_menu_string(ascii_images["drink_menu_string"], 0, False), 1, False), 2, True), """
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         
  ╔═══════════════════════════════╗
  ║ [2]  View Drink Options       ║
  ╚═══════════════════════════════╝

    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    

    [14] Exit                      

                                   

""")

    def test_update_menu_string_up_to_1(self):
        self.assertMultiLineEqual(
            update_menu_string(update_menu_string(ascii_images["drink_menu_string"], 0, False), 1, True), """
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝
  ╔═══════════════════════════════╗
  ║ [1]  Add Drink Options        ║
  ╚═══════════════════════════════╝
    [2]  View Drink Options        


    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    

    [14] Exit                      

                                   

""")

    def test_update_menu_string_down_to_bonus(self):
        self.assertMultiLineEqual(update_menu_string("""
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         

    [2]  View Drink Options        


    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    
  ╔═══════════════════════════════╗
  ║ [14] Exit                     ║
  ╚═══════════════════════════════╝
                                   

""", 13, False), """
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         

    [2]  View Drink Options        


    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    

    [14] Exit                      
  ╔═══════════════════════════════╗
  ║ [15] Bonus                    ║
  ╚═══════════════════════════════╝
""")

    def test_update_menu_string_up_to_14(self):
        self.assertMultiLineEqual(update_menu_string("""
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         

    [2]  View Drink Options        


    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    

    [14] Exit                      
  ╔═══════════════════════════════╗
  ║ [15] Bonus                    ║
  ╚═══════════════════════════════╝
""", 14, True), """
                                                        ╔╝╔╝
                                                        ║╔╝
  ██████╗  ██████╗        ██╗ ██╗    ██╗ TM     █╗████████████████╗
  ██╔══██╗ ██╔══██╗       ██║ ██║    ██║       █╔╝████████████████║
  ██████╔╝ ██████╔╝ ████╗ ██║ ██║ █╗ ██║       █║  ██████████████╔╝
  ██╔══██╗ ██╔══██╗ ╚═══╝ ██║ ██║███╗██║       ╚█   ████████████╔╝
  ██████╔╝ ██║  ██║       ██║ ╚███╔███╔╝         ╚██ ██████████╔╝
  ╚═════╝  ╚═╝  ╚═╝       ╚═╝  ╚══╝╚══╝           ╚██████████████╗
                                                   ╚═════════════╝

    [1]  Add Drink Options         

    [2]  View Drink Options        


    [3]  Add Team Members          

    [4]  Update Favourite Drink    

    [5]  View Team Members         


    [6]  Take Order                

    [7]  Produce Favourite Order   

    [8]  View Last Order           

    [9]  Distribute Last Order     

    [10] Clear Last Order          


    [11] Change Team Details       

    [12] Help                      

    [13] Logout                    
  ╔═══════════════════════════════╗
  ║ [14] Exit                     ║
  ╚═══════════════════════════════╝
                                   

""")


if __name__ == "__main__":
    unittest.main()