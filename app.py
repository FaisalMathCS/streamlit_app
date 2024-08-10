import streamlit as st
import pandas as pd
import numpy as np

st.logo('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPEAAADSCAMAAACsLdajAAABUFBMVEUAAAD/////0CD/ABL8/PwGBgb39/cICAgAAAP/0RvErkb90SDGrkj+0CT/0xvNDBoAAAfKyspKSkrwzziGhobf39/xCxcXAACmpqa4uLjx8fFdXV2SkpIABADy8vLn5+cfAwGQfzKRgCosLCyioqKMgi6ampobGxsAAA7IyMiOgia2trZDQ0NtbW1+fn43NzclJSVUVFR1dXXW1tYzMzMVFRVkZGT/4jEAABb/zS//2S8TARFgUCiUfTC1mzvStkHjxDJlXyqlkz3ZvjhEPx9yazDx3DVWSiPVwkh+cDM0LBhVRy/62RTy20ZOPx7kzi/YvhUcGAu/s0FCPyIzLyTv01H14ie7nkCWjSpNQBd9dCjtyTrp7N/83D2BcD0sIBtLPy2Qdi3KtCiqllDazklNDAzCFCGzDhzlEh14DxZoEBYsBASaezBvYDouKQ3g1SZSOhzYAAARpUlEQVR4nO1d/XvbNpIGFZKiwpClZSmVZMlsIkUf0ZclRbalNk5rp043K593s5febXLe7t71I9te7/7/324GIEUCJGU50Qf1HN+njW2RFPBiBoMBMBgSkiBBggQJEiRIkCBBggQJEiRIkCBBggQJEiRIkCBBggQJEiRIkOD/N5RtlrudwvvlQqGc3ULp2eymSyTIsjOSKOyDzVLO2VhqvrfJMgkSHkoyY6xK9Q0WXM1LDvLVDRYL6Eqywxh+ljdW7JHqlAv/qpulrEoeZOnZphTb9hUr5TdTJkIhdVenGePW0ow19q+D+QdLIjfXLIpN9mWurYHzck9ZlmbB/6TicCbIGT+ymk1rmS/I88WOPoXCHSEJ6C/3mOXwAqLNL790/4YmsCrEul3aY79mIT66/ndGQ2R8sMRDCgq1+dXzsxdfT6cnDNcvzp5+0wDmzSUIk2cf2dCrgFh0Z5mHrFfnFzfTqZFKGYBUCn/qGXM6vTj7trnMF2yHcZr+W+J6sRytXhVLg45KFIu8PNufmmYmpZt6Rk/pOjLOpCgy5snN/a+gSRTs6NHCTvNavaDYleKg1i6UlzYhllapQB8l3744MSdGKgoZIL3/3EKLRhbYsECxjTVLGYagnioFIEuDyEesinYKfN/OMqapRxJOGZOJYUwvH58SZZHV7nGjE/u1VHYVbw1QSDHIF1CMfkSrNMmr72YgX0NfwFg3aYPM9v+waIRWiC3LgdLlw+gG/2S0xeGBtnSkTtOh1zq7SRkZ3QRBLpAx/JcxUnpq+uI1PKZVIr6xEapi0tomM8dhApalXER5IF7N+uP1bIFsA7I2Zld/gM4cqdmD0Cqo4/UQJvmghKmlLoTerTWB8qPZxJjdhXEqM3sTPTg/C5HxLf3qU1AN0Wkm5UKolJVm8/50Yhp3kHEGLNhEv34dIeOBHNKPaRXWw3gYxVgOaWPNqjSb300zmYk5NaGbTpaVsjnVzat/ob63+J3HUhRj6XgtjMvhhVEp7wl8wZtoWhfgaaQm1y8fgaRhdFpgueYy1nUwYMbk5BV0ZZHxMLJ8aU1T9F40Y1Uw2Bb24QszZab067TVvNQNY7KMdpvG9E/70A/06StNERjnFhBeE+NOhFYzCJTJ6XemASp9/WereT5NGVMzs4ROG+bZ6Q9XoBipy78Kfbm+iPCatBrG/+giVdn2WS8QzxtDNyfm5WuNnJ8Y5nd/uT+9RcYZaBI9dUaa/3oDY7P59s9c2YWFhNflYXNqLcuqMFSUGvQuCyZ/FXI+M1JT4+aVRR6fZCY/WtbfZ7o+m0R0ZqCof30Bum9MH2nkm+9BO2Zv0RZQVwSaUnT2ZJVzN9c0OhGy5y+0LfGMZenwGd4EVrpi/X4CY+vEfELIu5NU6vKl1XxjZPaf/psZpc6zfat5kYHL339LyBl4LfrsAfgwjmq3AkI95Io+WhdjmLzMlxJzKHJezWW1g/KwLGt8NQGpZS605surSWr2hJz++/fG9J1FrsJHqYwxe29pX00nMCLf/KB9eWWCJz59d1phPWUk0FVhbMhL3mLqmnoxUaD4mlOmPQBuXYGxKstZQtBMv9HBe5rtv25aP8Kc/8pq/vXGzLwhza9OIrQ6pU8fEe1rdFfM+8Q6N5kRYCOUMEkEtIgnd1ldZgXm45AGykq5ONprYxkKermyqNng1Gvk3RTGmYx5bmln4H7MYEJ0oU9OXmqn+5moQdnIvAejDqNxJnXyilg3MEKZ+gVRKqT5HwJd2m2h9GMqeruGsljX6rH/ixUFZqXZQ0GvkTI53ae89DPy6gYq/jUhfzsxMjc/NM/NBa7X9I/k71P4OTHfQK83UyDuKbQVKQVGiBq0PatKtU+t5drmx0AznaaCTtMCoaDOIafZ4AXCNObcoAYqM3sxNXGItZrXILzp2wfTRU62+ag5PqHivvySvNORsX4FpqstSrhMm34uV6jT+gjTAqAEpzD8cVTilyUKxPoBdBprPkmZExhjzf2/nU1h+MmYM+ib0TI2bv7xn3gZevI/rHPQbhigZ+fQkwUJ91yy2PxMAhsEFDe2fVJW0RX4r5vLfcT1/jX75fKa/vX+/f77/QW4vnGvX/54tY/PvN//cWyBtfSrURc1bKMkBcoEp81ejUDEp01CV+dctzh0rqvRbYmwCxr/lAXf5jOP8gEzoFsEFj/yBuYq0SputTWXkxYE8S64v86/0n+Phv6b25OhkCxvPrcClPLIdb9GRPvp559//myF+EXxVubV6pZVmgHr4Lq9Q1L55d5q8fCniutzlY6Isma7vBwU6umrqHVp8vmHFTO+94uGu6joa5C1jrx3AUqZ9rU9Uvnnw1Uz/uBsvwDhdY+8ywP7VhmknCOVz1ZN+N69X6ltxHWl2BBmjm1Okp6RL1au1KDWOIEpxsBIc8Da9MD9+HX1hO99qJBuK26E2cRiQMg/18D44RdkHD/CTo1WPjZRxj9pa5wPfgKwTpU1dGMwXVpMJCxuAEKtKp89/PBw1fjwa0ULsdKatVR80AqRtiwtPQak0QmmEzdN+eK33377QsDnkaAV99zvqJI+r1gW/XqnmLTnjm8Sy6sZjdhysbLyF0aMrB5omb95+uSRiCfP//v5k4V4yuPx46eheOzH8+ePgkU9eh29y7wOxoT8fjMz55gFfomEruu33iNgRr92xn/37O3/bDLMGQzJhZExOAAV3QgFXdMRoUdifjXyVvzQNM9Jc3OUgfH/GsaCRSs/aCWXu/UOmMzON7kaohDrTDcNTs0yAEEdnQ9CrrAPQxF8JPSW2eU3y4WvroixQprnD+5zeAC4L37kXhCvOJ+GIvBlYXc8uP97TJYHNok4+GFxqMOG0ZLVlUPe3DmMuwJ6t7v3uFIcxGQiEYSCG6wicPl+VMj1ym1biohOws/yxXa7aDv3C1fjODl2oARjzSVZrbsxhP2CuMfuYH5eq1EuBe/Ix9g+KMEzI9Ko4VxB9PMBQvB3zv8dtYCUC7Fa0uOhYEwOX9+iIKBigDKLHvG+4kCMlB/EmDGAqy+N5fMTTlPK3I6zesRvxNP4Wv8d6sY53BHcabfDkC448jNWw2Kjcxzj9mbq/fHgtvSDodcKOeKUthVoE5A4F9a8xgj51eDgVoXkxuzQox3eGCfLdnwNtQvfyaBW6A1HPsIRpy3n8WkY9RF7xmWvF+bCriv+gLTw8HsvOFCW42ymKRSieJ0w4sSGr6uHtok/7jT2dosNyS4iDvfNQ9NlaRh+R92VsNSI92BMKGOvn0aED/piwyOOENfcFinE2MN0kVY8v+tWnY26o+jKmMRexGya43ohEWHPvtjhCMvlxp6u84Te6pBW5mpbCr/D51+Ej05jFtJMZ007wFhRvIDobtgNXCh+aMKHnNOLsztBmJqaZ05PzgfsTloIpg01TXggg56Vi+W2cQgUT0oBy6TwYZayNA4ypj4M1en4G2oHClonJqesOBc8Fs4Qiz0ZQ/TwDvkwvRNmiwE5Ooshap9wjA8C61h7wqMNxzEfxHh5K4i0W3FZlrljG+XAmo4s2ZxrllWZ1nd3ijCVctU9klSc2+ODvEDWQXE+B2643gm6nzuj0xQgn47KpAyKm8v2+92CLc2PSOXL3WGt5DEvFcu5Ya8+cldv0fvcJQkjoL59LomGX7Y1dk8rdDFXZuP4bkkYAc7D2A4hxIyVQv8LbxIVc6ztHmHmLhVD1+TnG0nB03nOwd7d8LVE0HD3XpjezucP4vE8pExTuu0kYcLq3WiFbCVVca2EiMcAcVdqhEt9MTgZ8LGgNT8InDuUD6n3WZfE1A+lLl032l3CKCysfjcvcZuG+FvpUBL7eJ6tAe1mH2ag2kkFli1GZPLwWsFzQ3ZXxkgY5NViy13DljoXsMRmR3MRqy0m3irc2tmZOWIoanTlcuQsWWbL7eBZ4nyx7OQ4PSjiqkkvvkEQtwAFVYJpBD2wq7bnOnt0PMzV2oh6bng8Pw/fKZTY+WUS47iPhQB1HtuHvrwlpWJUviGFHBdsZ3zaw6XO2i72ZTC4MF9so5PhLNPhvtuoVRbP/A9ybeptut0bdJ/uROweZdJXUUfTXofdc6NE7BEwJ/3WaMQyjDT8yS9ylP/a0l2sCSifLHhQMpdQq4BHLvFTmdLPSu4gPfCnDBqxfanwbcm4AgkfyLT2CumPXN9j6M9F5DB2xOrmOsMEvk6SKJxP7JIr0pVwBYTNGIbOnLDv3yv3My74tqoKYzf36QYT+X4yFBbJIePE3sZRqWczm9QKZzyiW+TQRCUnFTbr3vYOedh1tv4qVbEbt3CZ63iEZ0vtcMY2mzYyP6W85260yfb6ktesGM7eIkb60JX6NnKuDnHDSXbjFD3GNKVqMV/Gmxq1Q8zD5Bqyw/5uSHkesWWzjVPMSod+pKLkWvNlHr+MS44su2zda+AlbVQ3mMv347E3nyLs+QI67DLzuKrDWitfwqUdYKzao2K9m2Z7FfPZVZlUPe2PeWwTaqBvIafoS0KEwYYD760I4wZJN+aDzxHl6E6gC/4wOHl9aYpWAJocxCOMVS/JPvexLamjwtDZgWD9M32ca+dVaBpf7qk93xqnjAY/zn05zS3X1unbEBzRHXoqLtv5fIF0bNsN28p7ZlzGrPZ8fqpenDwRhftBjrjMaGwrNedIecQk56ru3HKh8S65nQHHNJwr+pO9bfLtDXdDmvR5wiCcPu6IFt1O7V/V8ttqSUrPo2FaNBxbSKtXj8+OTG9UkksjKkuFDMRF2iHp0p1F+kKVOun7r/GMnzlD8AhtW6MhMPYy6/aKo3yxx4rbBgaugTlEXgeSiOHc5RrsgcC5G3jGXToEt6gt74GrJuTkolOpNHYQ1gK5LVEeyqxXYk/shWTFlTsgVgznwMp1qnwWWZ5xmXQOa9QPGdrodInZMVWk7Ho2shqIzN8MOCWVAsd+aJZBtgSgFtgKLlvMFLxM+mfBMcfsxT4kmB8TpMy1QmEbQ9aIzzcnrkeDT5x2GYObyUbh45rroHgyLrXKHUq4X1BZA4SmBJX5zZyl3uewWnQCUuDqV6oK0fD5suM9d7r1dnHUJtl8q13oucte/br3HiMhnjUUW1gWWpx51x6zzZSWz5eS8jWfl+xTykaXnf5ynt1jGzHRyaMlJ2Jzwwh/7YBPTLRn1gV7JufbOW+Nmow7MLEQt9UxgCCtiAdERGx47gwVCm52exgRN1dacMhixEu2bZcitqKooqNhWpCiW95CR47sZ9Qxnu8PLhJT6NPuu0/Siv9NYUGs6/UC0QieyXTR9iftXKQKoYznqb+x0Q4iDjrSicnGEbU9WuD2E6IbJorxPJQTO0Y2qpT2FnyQCMNSFjZQIiKcIhn7jTDGwUU839g0XUS4whaEPX7RWt8G/+EXhUQFSG36dYsOipIaYIPJ9nwyBvLBexbiyDf/T4flrkZEHK9YL5BVl9WHCx/GM1mK/66Fb0UIoOAL9FEiNCQ/2E6sCJVktdvrim+n4ZYsFD4v7i2QS4RvLsFwtfBVrR1CtrT05WSx5qZ9CP7NEuJh1MUY8FzExmy5JW+KowiayxrfrMVViz8Bg/uMIf09DCoey+SEJ/YITIvqNvS2AM0tVks4g7vYXeRQE7OeirNuOw7xfOnA6oeY2yFwOCIcLN26/7m08Coaeqhi+yu5YJmFqgeWZDBffUTcsZ9PV5SwEpiEF+PBmF9dlkPO4KbZDD/y7UwYn7nXCBgkTLbBH5wZxECp6fEATvNGIR4v1rO/cH55HJK5OGABRnEQMa1D2bfSEf6WOMqmWqC7EvObJcd5oSGZES9J8JJpgIYcxWcLyl2hkSU7aseXqWO23OKnBuqocOxdDoGXMuWwE5etCRrL5Owb0RWbqPscVkfZbrmOKPcGLN9L9EshMArf2dtpKXEh7Lh8R8e54WD+V9SNwcT5zItZ+NWDeqEwxM4SG8Y+lrcHCtMXrYyR5Bh+udV/8ppIiVekuULrvpZXHyi0Fdf+9pePQYx0LkGCBAkSJEiQIEGCBAkSJEiQIEGCBAkSJEiQIEGCBAkSJEiQ4P8AQqaV5MOvWCcAAAAASUVORK5CYII=')

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