# QRSecure
QR Secure: A mobile application that uses machine learning and security validation functions to prevent interaction with malicious QR codes.

The ML model within this application uses the urldata.csv dataset from Kaggle.

# User instructions
Upon launch of the application, the user will be presented with a QR code scanner, which can be used on any QR or barcode, Once the scan has finished the application will present the user with a report page,
here the application will advise the user if they should continue to the content embedded within the QR code or return to the scanner. This decision is determined by the ML model prediction and two security validation functions. The user can then return to the scanner or continue to the embedded URL which will be opened with the device's default browser.
