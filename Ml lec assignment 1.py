import streamlit as st 
import pickle
import pandas as pd 
import sklearn

st.title("Breast Cancer type prediction")
st.info("Please fill out the sections below")
st.sidebar.header("Tumor type")

clf=pickle.load(open(r"C:\Users\20106\Downloads\Breast_cancer_1.sav",'rb'))

radius_mean=st.text_input('radius_mean')
texture_mean=st.text_input('texture_mean')
perimeter_mean=st.text_input('perimeter_mean')
area_mean=st.text_input('area_mean')
smoothness_mean=st.text_input('smoothness_mean')
compactness_mean=st.text_input('compactness_mean')
concavity_mean=st.text_input('concavity_mean')
concave_points_mean=st.text_input('concave points_mean')
symmetry_mean=st.text_input('symmetry_mean')
fractal_dimension_mean=st.text_input('fractal_dimension_mean')
radius_se=st.text_input('radius_se')
texture_se=st.text_input('texture_se')
perimeter_se=st.text_input('perimeter_se')
area_se=st.text_input('area_se')
smoothness_se=st.text_input('smoothness_se')
compactness_se=st.text_input('compactness_se')
concavity_se=st.text_input('concavity_se')
concave_points_se=st.text_input('concave points_se')
symmetry_se=st.text_input('symmetry_se')
fractal_dimension_se=st.text_input('fractal_dimension_se')
radius_worst=st.text_input('radius_worst')
texture_worst=st.text_input('texture_worst')
perimeter_worst=st.text_input('perimeter_worst')
area_worst=st.text_input('area_worst')
smoothness_worst=st.text_input('smoothness_worst')
compactness_worst=st.text_input('compactness_worst')
concavity_worst=st.text_input('concavity_worst')
concave_points_worst=st.text_input('concave points_worst')
symmetry_worst=st.text_input('symmetry_worst')
fractal_dimension_worst=st.text_input('fractal_dimension_worst')


dataset_new=pd.DataFrame({'radius_mean':[radius_mean],'texture_mean':[texture_mean],
'perimeter_mean':[perimeter_mean], 'area_mean':[area_mean],
'smoothness_mean':[smoothness_mean],'compactness_mean':[compactness_mean],'concavity_mean':[concavity_mean],
'concave_points_mean':[concave_points_mean],'symmetry_mean':[symmetry_mean],'fractal_dimension_mean':[fractal_dimension_mean],
'radius_se':[radius_se],'texture_se':[texture_se],'perimeter_se':[perimeter_se],'area_se':[area_se],'smoothness_se':[smoothness_se],
'compactness_se':[compactness_se],'concavity_se':[concavity_se],'concave_points_se':[concave_points_se],'symmetry_se':[symmetry_se],
'fractal_dimension_se':[fractal_dimension_se],'radius_worst':[radius_worst],'texture_worst':[texture_worst],
'perimeter_worst':[perimeter_worst],'area_worst':[area_worst],'smoothness_worst':[smoothness_worst],'compactness_worst':[compactness_worst],
'concavity_worst':[concavity_worst],'concave_points_worst':[concave_points_worst],'symmetry_worst':[symmetry_worst],
'fractal_dimension_worst':[fractal_dimension_worst]},index=[0])


Confirm_button=st.sidebar.button('Confirm')
if Confirm_button:
    result=clf.predict(dataset_new)
    if result == 0:
        st.sidebar.write('Benign Tumor')
        
    else:
        st.sidebar.write('Malignant Tumor')
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtmx087PqIwk2ZZsadyKV8d1mdWhhP-Q-qAZ8pTrUCXA&s',width=250)


