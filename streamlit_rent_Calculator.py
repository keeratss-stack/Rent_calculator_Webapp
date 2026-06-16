import streamlit as st

st.title("Rent Calculator")
rent=st.number_input("enter the total rent amount:",min_value=0)
security_deposit=st.number_input("enter the security deposit if applicable:",min_value=0)
electricity=st.number_input("enter the electricity bill amount:",min_value=0)
water=st.number_input("enter the water bill amount:",min_value=0)
miscellaneous=st.number_input("enter the miscellaneous charges amount:",min_value=0)
total_persons=st.number_input("enter the total number of persons:",min_value=0)
if st.button("calculate"):
    if(security_deposit>0):
        total_amount_Fm=rent+security_deposit+electricity+water+miscellaneous
        total_amount_per_person=total_amount_Fm/total_persons
        st.success(f"the total amount to be paid in 1st month: ${ total_amount_Fm:,.2f}")
        st.success(f"total rent per person for first month would be: ${total_amount_per_person:,.2f}")

        total_amount_after_Fm=total_amount_Fm-security_deposit
        total_amount_per_person_after_Fm=total_amount_after_Fm/total_persons
        st.info(f"the total amount to be paid after first month: ${ total_amount_after_Fm:,.2f}")
        st.info(f"total rent per person after first month would be: ${total_amount_per_person_after_Fm:,.2f}")


    else:
        total_amount=rent+electricity+water+miscellaneous
        total_amount_per_person=total_amount/total_persons
        st.success(f"the total amount to be paid: ${total_amount:,.2f}")
        st.success(f"total rent per person would be: ${total_amount_per_person:,.2f}")

