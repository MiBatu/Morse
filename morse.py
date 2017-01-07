# Program to convert words and strings to morse code.
# Creating the Class Morse with .conversion method.
# As an argument use string with [A-Z,a-z,0-9],[.,:;()'-/?!@] 
# to convert it to morse code.

class Morse():
  def __init__ (self):
    self = self
    
  def conversion (text):
    string = ""
    dict_all = {" ":" ", "A":"._", "B":"_...", "C":"_._.", "D":"_..",
            "E":".", "F":".._.", "G":"__.", "H":"...", "I":"..",
            "J":".___", "K":"_._", "L":"._..", "M":"__", "N":"_.",
            "O":"___", "P":".__.", "Q":"__._", "R":"._.", "S":"...",
            "T":"_", "U":".._", "V":"..._", "W":".__", "X":"_.._",
            "Y":"_.__", "Z":"__..", "1":".____", "2":"..___",
            "3":"...__", "4":"...._", "5":".....", "6":"_....",
            "7":"__...", "8":"___..", "9":"____.", "0":"_____",
            ".":"......", ",":"._._._", ":":"___...", ";":"_._._.",
            "(":"_.__._", ")":"_.__._", "'":".____.", "-":"_...._",
            "/":"_.._.", "?":"..__..", "!":"__..__", "@":".__._."}
    error_letter = "........"

    text = text.upper()
    for i in text:
      if i in dict_all:
        string += (" " + dict_all[i])
      else:
        string += (" " + error_letter)
      
    return str(string)

text_input = str(input ("Write a text to convert to morse: "))
print ("Text on morse: " + Morse.conversion(text_input))
