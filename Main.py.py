# Import being used to create scanner
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar # Import to allow process bar
from kivy.uix.popup import Popup # Import to allow popup window
from kivy.uix.label import Label # Import to allow lables for GUI
from kivy.app import App 
import kivy # Import for kivy applications
from kivy.uix.gridlayout import GridLayout # import form Window layout
from kivy.uix.textinput import TextInput # Allow user input on GUI
from kivy.uix.button import Button # Import for buttons
from kivy.properties import ObjectProperty 
from kivy.graphics import Color, Ellipse, Rectangle # Import for graphics
from pyzbar.pyzbar import ZBarSymbol
import webbrowser # Import to open browser
from SSLCheck import * # Import to file allow certificate check
from DetectingMalisiouseUrlsWithML import * # Import ML file to scan url.
from UrlValidationScan import * # Import url validation function.

# Multi line string to importing ZBarCam to access device camera.
# Defining layout of camera window.
# Defining object to decode QR codes.

Scanner = """
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
#:import ZBarCam kivy_garden.zbarcam.ZBarCam

MDBoxLayout:
    orientation: 'vertical' 
    ZBarCam: 

        id:qrcodecam
        code_types:ZBarSymbol.QRCODE.value,ZBarSymbol.EAN13.value
        on_symbols:app.DecodeQr(*args)
		
"""
# Main class for application
class QrSecureScanner(MDApp):
	def build(self):
		self.root = Builder.load_string(Scanner)
    
    # QR code will be decoded if present.
	def DecodeQr(self,instance, symbols):
		if not symbols == "":
			for symbol in symbols:
				pass

		# Defining function to make link value global
				
			def print_global_link():

				global link
				link = symbol.data.decode()

		# Snackbar defining styling and text displayed from decoded QR.
		# Adding message while processing.
			
				Snackbar(
					text="Scanning.....",
					font_size=20
				
				).open()
				
		# Printing global value and passing value into variable for use in scanning functions
		print_global_link()
		ScanThisUrl = link 
		print(ScanThisUrl)

		# Calling function into Main.py

		# Calling SSL certifcate checker funciton form SSLCheck file and passing url as argument into variable as a string.
		CertScanResult = IsSslVaild(ScanThisUrl)
		outputScan1 = str(CertScanResult)
	
		# Calling funciton from ML programme to scan provided url and return label into variable as a string.
		MLUrlScan = ML_Prediction(ScanThisUrl)
		outputScan2 = str(MLUrlScan)

		# Calling function from url validation scan file that uses a python import to determine if the url is formatted correctly. > into a variable.
		FormatUrlScan = ValidatorsScan(ScanThisUrl)
		outputScan3 = str(FormatUrlScan)
		
		CWarning = " " # Warning message empty variable to change on condition.
		RWarning = " " # Warning message empty variable to change on condition.
		
		# If statment to change warnings dependent on if the URL is safe.
		if outputScan1 == "Clear" and outputScan2 == "Clear" and outputScan3 == "Clear":
			CWarning = " "
			RWarning = " "
		else:
			CWarning = "[Not Advised]"
			RWarning = "[Advised]"

			
		global url # Defining variable as global to access in functions
		url = str(ScanThisUrl) # Stored url from QR Code derived from scan
		
		# Defining the first grid layout for the popup where title will be situated
		TopGrid = GridLayout(cols=1) # one column long 

		# Defining Embedded grid to sit within topgrid, allowing the above grid to span whole screen
		EmbeddedGrid = GridLayout(cols=2) # two column long

		# Adding title to top grid to 
		TopGrid.add_widget(Label(text="Scan Results for:",
        font_size=30, # defining size
        size_hint_y = None,
        height=50)
        )

		# Displaying the scanned URL by passing the variable into a string.
		TopGrid.add_widget(Label(text=url,
        font_size=15, 
        size_hint_y = None,
        height=50)
        )

		# Adding text next to the returned value from URL scans, adding the three scans into the middle grid to be presented in two columns.
		EmbeddedGrid.add_widget(Label(text="ML URL Scan: "))
		EmbeddedGrid.add_widget(Label(text=outputScan2))

		EmbeddedGrid.add_widget(Label(text="URL Format Scan: "))
		EmbeddedGrid.add_widget(Label(text=outputScan3))
	
		EmbeddedGrid.add_widget(Label(text="PKI Certificate Scan: "))
		EmbeddedGrid.add_widget(Label(text=outputScan1))
	
		# Applying the middle grid to the topgrid which is then called as content for the popup.
		TopGrid.add_widget(EmbeddedGrid)
	
		# Defining a popup page for the resutls
		Resultpopup = Popup(
			
			title="QRSecure", content=TopGrid,  # Defining a title and linking the contents to the topgrid which has the middle and bottom grid applied via widgets.
		)

		# Defining contine button with dynamic warning dependent on condition
		TopGrid.submit = Button(text="Continue " + CWarning, 
		background_normal="", # As default is grey, first have to set colour ot none.
		background_color =(90/255,189/255,242/255), # Defining button colour
        font_size=32,
        size_hint_y = None, # Defining position and size
        height=80,
        )

		# If pressed call con function to contine to URL
		TopGrid.submit.bind(on_press=self.con)
		TopGrid.add_widget(TopGrid.submit) # Apply to GUI

		TopGrid.add_widget(Label(size_hint_y = None, height=3)) # Label to seperate buttons.

		# Defining return button with dynamic warning dependent on condition
		TopGrid.submit = Button(text="Return " + RWarning, 
		background_normal="",
		background_color =(90/255,189/255,242/255), 
        font_size=32,
        size_hint_y = None, # Defining position and size
        height=80,
        )

		# If return buttoon is pressed dismiss the popup window.
		TopGrid.submit.bind(on_press=Resultpopup.dismiss)
		TopGrid.add_widget(TopGrid.submit) # Apply to GUI

		Resultpopup.open() # Open the popup page

	# defining funciton to open url stored in variable on device native browser 
	def con(self, instance):
		webbrowser.open_new(url) # Accessig global variable 


if __name__== "__main__":
    QrSecureScanner().run()