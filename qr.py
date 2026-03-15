import streamlit as st 
import qrcode

st.title("QRcode")

qr=st.text_input("Enter The Link")
is_clicked=st.button("Generate QR code",type='secondary')

if is_clicked:
    if qr!="":
        img=qrcode.make(qr)
        img.save("qr.png")


        st.image("qr.png",caption="Your QR code")
        st.success("Your QR Code is Succesfully Generated")

    else:
        st.warning("Enter SomeThing")