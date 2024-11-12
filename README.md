# streamlit
Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.



#
#### Reference:
- [KGP Talkie-Playlist-python-stremalit](https://www.youtube.com/@KGPTalkie)
- [Python subprocess in a deployed Streamlit app](https://docs.streamlit.io/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app)
- [Streamlit Shell Script Runner](https://www.linkedin.com/pulse/streamlit-shell-script-runner-harish-panduranga-rao/)
- [Streamlit-Google-Auth](https://pypi.org/project/streamlit-google-auth/)
- [StreamlitGAuth](https://pypi.org/project/StreamlitGAuth/2.0.9/)
- [streamlit-navigation-menu](https://github.com/Sven-Bo/streamlit-navigation-menu.git)
- [Layout design in Streamlit](https://www.youtube.com/watch?v=0ZL-rK-IZIU)
- [Session States In Streamlit |](https://www.youtube.com/watch?v=gHeBtPLhBJE&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=42)
- [Cache In Streamlit ](https://www.youtube.com/watch?v=kOgSasvvxOg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=43)

- https://www.youtube.com/watch?v=G4c-LmdJTYQ
- https://www.youtube.com/watch?v=9n4Ch2Dgex0

  ---
  **Streamlit-এ কন্ডিশনাল স্টেটমেন্ট এবং অন্যান্য ফাংশন ব্যবহার**

Streamlit-এ কন্ডিশনাল স্টেটমেন্ট ব্যবহার করে আপনি আপনার অ্যাপ্লিকেশনকে ইন্টারেক্টিভ এবং ডাইনামিক করে তুলতে পারেন। এতে আপনি নির্দিষ্ট শর্ত পূরণ হলে কিছু বিশেষ কাজ করতে পারেন।

**কন্ডিশনাল স্টেটমেন্টের উদাহরণ:**

**1. `if` স্টেটমেন্ট:**
```python
import streamlit as st

user_age = st.number_input("আপনার বয়স দিন")

if user_age >= 18:
    st.write("আপনি ভোট দিতে পারবেন")
else:
    st.write("আপনি এখনো ভোট দিতে পারবেন না")
```

**2. `elif` স্টেটমেন্ট:**
```python
import streamlit as st

user_grade = st.number_input("আপনার গ্রেড পয়েন্ট দিন")

if user_grade >= 4.0:
    st.write("আপনি সেরা ছাত্র")
elif user_grade >= 3.5:
    st.write("আপনি ভালো ছাত্র")
else:
    st.write("আপনাকে আরও চেষ্টা করতে হবে")
```

**অন্যান্য ফাংশন এবং প্রোগ্রামিং টেকনিক:**

**1. `with` ব্লক:**
```python
import streamlit as st

user_choice = st.selectbox("একটি অপশন নির্বাচন করুন", ["অপশন A", "অপশন B"])

if user_choice == "অপশন A":
    with st.expander("অপশন A এর বিস্তারিত"):
        st.write("অপশন A সম্পর্কে বিস্তারিত তথ্য")
else:
    with st.expander("অপশন B এর বিস্তারিত"):
        st.write("অপশন B সম্পর্কে বিস্তারিত তথ্য")
```

**2. লুপ:**
```python
import streamlit as st

for i in range(5):
    st.write(f"নম্বর {i+1}")
```

**3. ফাংশন:**
```python
import streamlit as st

def greet(name):
    st.write(f"হ্যালো, {name}!")

user_name = st.text_input("আপনার নাম দিন")
greet(user_name)
```

**4. কাস্টম কম্পোনেন্ট:**
Streamlit-এ আপনি কাস্টম কম্পোনেন্ট তৈরি করতে পারেন যা আপনার অ্যাপ্লিকেশনকে আরও মডুলার এবং পুনঃব্যবহারযোগ্য করে তোলে।

**Remember:**
* Streamlit অটোমেটিক্যালি উইজেটের মান আপডেট করে যখন ব্যবহারকারী ইন্টারেক্ট করে।
* Session state ব্যবহার করে আপনি পেজ লোডের মধ্যে মান সংরক্ষণ করতে পারেন।
* কাস্টম ফাংশন তৈরি করে আপনি জটিল কন্ডিশনাল লজিককে এনক্যাপসুলেট করতে পারেন।

এই ধরনের কৌশল ব্যবহার করে আপনি ইন্টারেক্টিভ এবং ডাইনামিক Streamlit অ্যাপ্লিকেশন তৈরি করতে পারবেন।

#

**অবশ্যই, স্ট্রিমলিটে আরও অনেক ধরনের স্টেটমেন্ট এবং ফাংশন আছে যা আপনার অ্যাপ্লিকেশনকে আরও জটিল এবং কার্যকরী করে তুলতে পারে।**

**লুপ:**

  * **for লুপ:** কোনো নির্দিষ্ট সংখ্যকবার কোনো কাজ করতে হলে for লুপ ব্যবহার করা হয়।
  * **while লুপ:** কোনো শর্ত সত্য থাকতে পর্যন্ত কোনো কাজ চালিয়ে যেতে হলে while লুপ ব্যবহার করা হয়।

**উদাহরণ:**

```python
import streamlit as st

for i in range(5):
    st.write("নম্বর", i+1)

i = 1
while i <= 5:
    st.write("নম্বর", i)
    i += 1
```

**ফাংশন:**

  * **কাস্টম ফাংশন:** আপনি নিজের প্রয়োজন অনুযায়ী ফাংশন তৈরি করতে পারেন।
  * **লাইব্রেরি ফাংশন:** নামপাই, পান্ডাস, ম্যাটপ্লটলিব ইত্যাদি লাইব্রেরির ফাংশন ব্যবহার করে আপনি ডেটা বিশ্লেষণ, চার্ট তৈরি ইত্যাদি কাজ করতে পারেন।

**উদাহরণ:**

```python
import streamlit as st
import pandas as pd

def greet(name):
    st.write(f"হ্যালো, {name}!")

user_name = st.text_input("আপনার নাম দিন")
greet(user_name)

# ডাটা লোড করে দেখানো
df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
st.dataframe(df)
```

**অন্যান্য:**

  * **with ব্লক:** কোডের বিভিন্ন অংশকে আলাদা করে দেখানোর জন্য with ব্লক ব্যবহার করা হয়।
  * **session state:** পেজ রিফ্রেশ হলেও কিছু মান ধরে রাখতে session state ব্যবহার করা হয়।
  * **কেশ কন্ট্রোল:** ব্যবহারকারীর ইনপুটের ভিত্তিতে বিভিন্ন কাজ করতে কেশ কন্ট্রোল ব্যবহার করা হয়।

**উদাহরণ:**

```python
import streamlit as st

if st.button('ক্লিক করুন'):
    st.write("আপনি বোতাম ক্লিক করেছেন")
```

**এছাড়াও Streamlit-এ অনেক ধরনের উইজেট আছে যা ব্যবহার করে আপনি ইন্টারেক্টিভ অ্যাপ্লিকেশন তৈরি করতে পারেন:**

  * **Slider:** সংখ্যা নির্বাচন করার জন্য
  * **Checkbox:** একাধিক অপশন সিলেক্ট করার জন্য
  * **Radio button:** একক অপশন সিলেক্ট করার জন্য
  * **Selectbox:** ড্রপডাউন মেনু থেকে একটি অপশন নির্বাচন করার জন্য
  * **Text input:** টেক্সট ইনপুট নেওয়ার জন্য

**আপনি কি কোনো বিশেষ ধরনের ফাংশন বা উইজেট সম্পর্কে জানতে চান?**

**আপনার প্রয়োজন অনুযায়ী আরও বিস্তারিত জানার জন্য Streamlit-এর ডকুমেন্টেশন দেখতে পারেন:** [https://docs.streamlit.io/](https://www.google.com/url?sa=E&source=gmail&q=https://docs.streamlit.io/)

**আপনি কোন ধরনের অ্যাপ্লিকেশন তৈরি করতে চাচ্ছেন, তার উপর নির্ভর করে আমি আপনাকে আরও বিস্তারিত তথ্য দিতে পারি।**

---
