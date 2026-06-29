import streamlit as st
st.title("Password Analyser")
password=st.text_input("enter password",type="password")
#st.button("validate")
if st.button("validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
    if len(password)>=8 and upper and lower and special and digit:
        st.success("Strong Password.. Thank you")
    else:
        st.error("Invalid Password")
        if len(password)<8:
            st.write("password must contaim at least 8 characters")
        if not upper:
            st.write("password must contain at least upper character")
        if not lower:
            st.write("password must contain at least lower character")
        if not digit:
            st.write("password must contain at least digit character")
        if not special:
            st.write("password must contain at least special character")
            
            

            
            


