 # install qrcode
# install pillow
import qrcode
#import pi
 

# taking upid as in a input
upi_id = input("Enter your upi id : ")


#upi://pay?pa =UPI_ID&pn= NAME&am= AMOUNT&cu=CURRENCY&tn=MESSAGE

#defining the payment url based on upi id and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'

# create qr codes for each payment app
phone_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code in our file png format
phone_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


# display the qr codes (you may neeed to install pillow library)
phone_qr.show()
paytm_qr.show()
google_pay_qr.show()