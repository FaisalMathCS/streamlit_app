import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout='centered')

st.markdown("""
    <style>
    .custom-title {
        font-size: 70px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="custom-title">هل فيه شقق رخيصة بالرياض؟</p>', unsafe_allow_html=True)
st.image('Meme.png')


Welcome_text = '''
<div style="text-align: Center"> 
أكيد أنت الحين تسأل نفسك: "كيف ألقى شقة سعرها معقول وبمميزات تناسب احتياجاتي، في حي كويس وياليت لو كان قريب من شغلي الجديد؟" للأعزاء اللي ناوين ينقلون للرياض لبداية جديدة، بسهل عليكم الأمور وأعرض لكم أسعار الشقق في الرياض من زوايا مختلفة. بساعدك تحصل اللي يناسبك :).
</div>
'''
st.html(Welcome_text)





second = '''
<div style="text-align: right"> 
بالبداية أول ما يخطر على بال الشخص اللي راح يسكن في مكان جديد هو الحي وأسعار الشقق فيه, هنا بعرض لك الأسعار المتفاوتة لمعظم أحياء الرياض أو خلينا نقول أشهر الأحياء القريبة من أماكن العمل.
</div>
'''

st.html(second)

#First
st.image('Q1-st.png')




third = '''
<div style="text-align: right"> 
يمكن تسأل الحين: "وش هي الأحياء الأغلى والأرخص؟" البيانات تقول إن حي الملقا من أغلى الأحياء في أسعار الشقق. ممكن تسأل نفسك ليه، وأنا نفسي محتار مثلك. أما حي المناخ، فهو من الأحياء الأرخص. يمكن أول مرة تسمع عنه، لكن لا تشيل هم، بعطيك أرخص 5 أحياء وأغلى 5 أحياء عشان تقارن بينهم وتختار اللي ودك فيه.</div>
'''

st.html(third)

#Second
col1, col2 = st.columns(2)

# Display images in the columns
with col1:
    st.image('Q2_1.png', caption='أغلى')

with col2:
    st.image('Q2_2.png', caption='أرخص')
forth = '''
<div style="text-align: right"> 

لسا باقي مو متأكد من اختيارك؟ ممكن تفكر بالعوامل اللي تأثر على سعر الشقة؟ هنا بوضح لك إيش العوامل اللي ممكن تأثر على سعر الشقة, هل الدور الأول يفرق عن الثاني, هل عدد الغرف تفرق؟ وأكثر!</div>
'''

st.html(forth)

# Third
st.image('Q3-st.png')



fifth = '''
<div style="text-align: right"> 

طيب عزيزي القارئ هل ودك تريح نفسك وتشتري شقة مؤثثة؟ لكن ودك تعرف أسعارها وفرقها عن الغير مؤثثة؟ البيانات هنا توضح لك أن…..

</div>
'''

st.html(fifth)

st.image('Q4-st.png')

sixth = '''
<div style="text-align: right"> 
بالنهاية أتمنى أنك استفدت وهوّنت عليك ضغط النقل لعاصمة المستقبل الحبيبة الرياض.

</div>

'''

st.html(sixth)