# Streamlit Notes

## Table of Contents
- [Streamlit](#streamlit)
- [st.write()](#stwrite)
- [Data flow](#data-flow)
- [Streamlit Elements](#streamlit-elements)
  - [Text Elements](#text-elements)
  - [Data Elements](#data-elements)
  - [Chart Elements](#chart-elements)
  - [Form Elements](#form-elements)
- [Session State](#session-state)
- [Callback](#callback)
- [Layouts](#layouts)
- [Widgets](#widgets)
  - [Id / Key](#id--key)
  - [Widgets’ state](#widgets-state)
- [Caching](#caching)
- [Fragments](#fragments)
- [Multi-pages app](#multi-pages-app)

# Streamlit

- Simple and powerful UI library → allows to build entire website using python
- Install streamlit
    
    ```python
    $ pip install streamlit
    ```
    
- To run,
    
    ```python
    streamlit run .\file_name.py
    ```
    
- Hot reload → If source code is changes then it will automatically update the UI
- Anything written in the file will get rendered

```python
import streamlit as st

"Suriya"
29 + 13 if 0 else 29 - 13  # 16
```
## st.write()

- Magic command in streamlit
- A function → used to add anything to a web app
- Will automatically determine how to write the given content(python object or numpy value or json, etc,.) based on its type

```python
import streamlit as st

st.write("Hello")
```

# Data flow

- Anytime something must be updated on the screen, streamlit reruns the entire script from top to bottom
- Whenever some event occurs that changes the state of our application (like a button press) → rerun the entire python file

```
button1 = st.button("Button 1")
print("First:", button1)

button2 = st.button("Button 2")
print("Second:", button2)
```

- Initially, both buttons are in False state
    
    *First: False
    Second: False*
    
- When first button is clicked, it’s state becomes True → reruns the entire python file
*First: True
Second: False*
- When the second button is clicked, it’s state become True → reruns the entire python file, which changes the first button state back to False
*First: False
Second: True*

# Streamlit Elements

## Text Elements

```python
import streamlit as st

st.title("Pokemon")
st.header("Ash and his Pokemons")
st.subheader("A day Ash got his first pokemon - pikachu")
st.markdown("_Pikachu_ - a pokemon no one dared to pick")
st.caption("But became friend with Ash Ketchum")

st.image("static/pokemon-first-episode.jpg", caption="Ash and Pikachu first meeting")
st.divider()   # hr tag

code_ex = """
def greet(pokemon):
    return f"Hello {pokemon}. I am Ash Ketchum from palet town"
"""

st.html("<p> Sample greet() code<p>")
st.code(code_ex, language="python")
```

## Data Elements

- dataframe(data) → can enlarge, search, download, sort by columns
- data_editor(data) → same as dataframe, and allows to edit data directly
- table(data) → static table with no features
- metric → label and value pairs, highlights the value; ex: no.of rows, avg can be displayed
- json(data) → similar to python’s dict view in write()

## Chart Elements

- can be downloaded as png, svg and interacted(zoom)
- area_chart, bar_chart, line_chart, scatter_chart, geo-location map (map()), pyplot chart (using matplotlib)

## Form Elements

```jsx
st.form(key, clear_on_submit=False, *, enter_to_submit=True, border=True, width="stretch", height="content")
```

- Input - text_input(), number_input()
- Text area - text_area()
- Date - date_input()
- Time - time_input()
- Button - button()
- Range - select_slider(label, options = [])
- Check box - checkbox()
- Radio button - radio(label, [options])
- Select dropdown list - selectbox(label, [options])
- Links
- Submit button - form_submit_button()
    - used with ***with st.form()***
    - ***with*** → prevents rerunning the scripts when anytime a widget or something inside the form changes; collectively collect the data rather rerunning if any field changes
    - *key* can be specified → used to uniquely identify the form
    - Required one
- Balloons - st.balloons()

```python
with st.form(key="student_data_form"):
    student_data["dob"] = st.date_input("Date of Birth:", min_value = min_date, max_value= max_date)
    
    if(student_data["dob"]):
        age = max_date.year - student_data["dob"].year
        st.write(f"You are {age} old") 
        **# get updated only after submitting, because we are not rendering only when submit is clicked
        # can use session state**
    submit_button = st.form_submit_button()
```

> Dynamic updation of different components inside the form is not possible as it requires the rerun
Only after the submit → trigger the rerun
→ need session state for that
> 

## Session State

- used to store values within the same user session
- By refreshing the page, the session will get changed → each session is per user, per run or per instance of the kind of web page
- Without session state
    
    ```python
    import streamlit as st
    
    counter = 0
    
    # will never get updated
    # When the button is clicked, the file reruns -> set counter value back to 0
    st.write(f"Counter value: {counter}")
    
    if st.button("Increment by 1"):
        counter += 1
        st.write(f"Counter incremented to: {counter}")
    else:
        st.write(f"Counter stays at: {counter}")
    ```
    
- By using session state
    
    ```python
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    
    if st.button("Increment"):
        st.session_state.counter+=1 
        st.write(f"Counter value incremented: {st.session_state.counter}")
    
    if st.button("Reset"):
        st.session_state.counter = 0
        
    st.write(f"Counter value: {st.session_state.counter}")  
    
    # Until Refresh, the counter value is maintained   
    ```
    

## Callback

- A function that can be triggered when an event occurs
- Callback → runs before any other code on the next rerun
- If we need to do something at the beginning of the rerun ie. immediately after an interaction , callback can be used → callback is triggered before anything else

```python
import streamlit as st

# the app reruns top to bottom on every user interaction

if "count" not in st.session_state:
    st.session_state.count = 0

st.write("Count:", st.session_state.count)

if st.button("Increase"):
    st.session_state.count += 1

if st.button("Reset"):
    st.session_state.count = 0
```

After clicking Increase button twice -> the count value will become as 1
Because, Clicking a button triggers a rerun of the entire script
This time, the button value is True so it updates the counter value
write is above the if statement, so it shows the prev value

```python
def increase():
    st.session_state.count_value += 1

def reset():
    st.session_state.count_value = 0
    
if "count_value" not in st.session_state:
    st.session_state.count_value = 0

st.write("count_value:", st.session_state.count_value)

st.button("Increase count_value", on_click=increase)
st.button("Reset count_value", on_click=reset)
```


# Layouts

## Sidebar

- st.sidebar.title(), st.sidebar.write(), st.sidebar.text_input()
- Use st.sidebar.command
- Sidebar is resizeable

## Tabs

- st.tabs([list of tab names])
- Can use ‘with’ keyword to do context specific functions

## Columns

- st.columns(n) → where n is no.of columns

```jsx
st.columns(spec, *, gap="small", vertical_alignment="top", border=False, width="stretch")
```

- Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects
- To add elements to the container, ‘with’ is used
- Can call methods directly on the returned objects

## Container

- st.container()

```jsx
st.container(*, border=None, key=None, width="stretch", height="content", horizontal=False, horizontal_alignment="left", vertical_alignment="top", gap="small")
```

- By default, width matches the width of the parent container, height matches the height of its content
- Using a horizontal alignment → similar to flex box
- For vertically scrolling container set height property

## Empty Container

- Placeholder → where we can render dynamic content; reserves a spot in the layout
- st.empty()
- Used to hold a single element → to replace multiple elements in succession
- Used for progress messages, timers or loading indicators

## Expanders

- toggle content → multiple pieces of content
- Gives dropdown view
- Insert a multi-element container that can be expanded/collapsed
- All content within the expander is computed and sent to the frontend, even if the expander is closed

```jsx
st.expander(label, expanded=False, *, icon=None, width="stretch")
```

- *icon(str | None)* – Optional icon next to the expander label.
    - *None* → no icon (default)
    - Emoji → e.g. ‘`🔥`', ‘`🚨`'
    - Material icon → e.g.  “:material/thumb_up:” (uses *rounded* Material Symbols).

## Popover

- Insert a popover container
- Consists of a button-like element and a container that opens when the button is clicked
- Opening and closing the popover doesn’t trigger a rerun. Interacting with widgets inside of an open popover will rerun the app while keeping the popover open

## Tooltip

- Tooltip can be added to buttons with “help” attribute

> The only elements that aren't supported using object notation are *st.echo*, *st.spinne*r, and *st.toast*. To use these elements, you must use *with* notation.


# Widgets

## Id / Key

- One that holds some kind of state, for example text_input, button
- All the widgets will have an auto-generated id or key based on the type of the element and then any parameters that we pass to it → this id/key is used to store its state
- Key/Id can be passed by using the key attribute
- If same type and exact same parameter are passed, then the automatically generated key will be same → error
- If a widget’s parameters are changed, so is the state of the widget

```python
import streamlit as st

**# Widget's Id is assigned based on its parameters
# Changing widget's parameter changes its id, so the state**

st.subheader("Value is not maintained")
min_value = st.slider("Set Min Value", 0, 50, 25)

slider_value = st.slider("Value", min_value, 100, min_value)
# when min_value is changed, the slider_value will also changed, state is not maintained
# Because -> parameters of the slider_value is changed when min_value is changed -> creates a new id

st.divider()

st.subheader("Slider Value is maintainer even when state is changed")
# Can use session_state variable to maintain its value
if "slider_value" not in st.session_state:
    st.session_state.slider_value = 25

minimum_value = st.slider("Set Minimum Value", 0, 50, 25)

st.session_state.slider_value = st.slider("Slider Value", minimum_value, 100, st.session_state.slider_value)

```

## Widgets’ state

- If Widget is no longer rendered on the screen, its state is destroyed
- When we stop rendering, then its internal state is removed from the session. And when we create that component again, it now has a new state
- Re-rendered widgets reset unless you bind them to st.session_state

```python
# If not rendered, internal state from the session is removed

checkbox = st.checkbox("Show Input Field")

if checkbox:
    user_input = st.text_input("Enter something: ")  # when checked again, it renders again
    # st.text_input() now resets its value to "" by default
    st.session_state.user_input = user_input
else:  # If unchecked, st.text_input() -> disappears and so its state
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input: {user_input}")
# here user_input is will get disappeared when it is checked again

**# Can be solved by, binding a session_state to user input**
 user_input = st.text_input("Enter something: ", value = st.session_state.user_input)
```

# Caching

- Long running functions run again and again, which slows down the app and Objects get recreated again and again, which makes it hard to persist them across reruns or sessions
- To cache a function, one of the two decorators can be used
    1. st.cache_data
    2. st.cache_resource 
- Whenever this function is called, it checks for
    1. Values of the input parameters
    2. Code inside the function
- First time call → Streamlit runs it and caches the result. On subsequent calls with the same parameters and code → returns the cached value instead of re-executing

## **cache_data**

- Used for immutable data
- Modifying the value won’t affect the cached value
- Returns a new copy of data at each function call → safe against mutations and race conditions
- Useful when loading a data frame from CSV, transforming a NumPy array, querying an API
- Implicitly uses *pickle* module (which is known to be insecure) → Only load data from trusted sites
- Mostly used as most data in python are serializable object (obj that can be converted to bytes via pickle)

## **cache_resource**

- Used for mutable data
- Allows modifications to the underlying resource
- Recommended way to cache Global resources like ML models, or database connections
- Shared across all reruns and sessions of an app without copying or duplication

### Controlling cache size and duration

**Time to Live (TTL)** → sets a time to live on a cached function. If that time is up the app will discard any cached values, and the function will be rerun

**max_entries** → sets the max number of entries in the cache. The oldest entry will be removed when a new entry is added to a full cache

**Spinner customization** → can be disabled, can use custom text by using *show_spinner*

> Note: Manual rerun → st.rerun()
Can force the app to rerun


# Fragments

- Way to rerun only certain portions of the User Interface and better organize of separate out the code
- Code block that is separated with decorator *@st.fragment* → will run independently from the rest of the application
- Helps to limit reruns to the particular scope(fragment)
- But we can force rerun the entire app by using *st.rerun(scope=”app”)*
- If we need to do dynamic update, better wrap that inside the fragment
- **Cannot return data from the fragment, if we need to then session_state can be used**
    - session_state → can be accessed globally
- If the fragment needs to be appear in the sidebar or another container, call the fragment function inside a context manager
    
    ```jsx
    with st.sidebar:
        fragment_function()
    ```
    
- When app rerun occurs, entire page reruns (including fragments), but the widgets remember their last values (internal session state)

### Automate fragment reruns

- ***run_every*** parameter causes the fragment to rerun automatically at the specified time interval
- Will continue even if the user is not interacting with the app

```python
@st.fragment(run_every="20s")
def filter_and_file():
		...
```

> **Using caching and fragments on the same function is unsupported**


# Multi-pages app

- Provides 2 built-in mechanisms for creating mutli-page apps
    1. Using *pages/* directory
    2. Using *st.Page* and *st.navigation*

## Page Terminology

A page has four identifying pieces as follows:

- **Page source**: This is a Python file or callable function with the page's source code.
- **Page label**: This is how the page is identified within the navigation menu.
- **Page title**: This is the content of the HTML *<title>* element and how the page is identified within a browser tab.
- **Page URL pathname**: This is the relative path of the page from the root URL of the app.

Additionly, a page can have two icons as follows:

- **Page favicon**: This is the icon next to your page title within a browser tab.
- **Page icon**: This is the icon next to your page label in the navigation menu.

## st.Page and st.navigation

- Preferred commands for defining multiple apps
- entrypoint file acts like a page router; Defining elements or widgets in entrypoint file, become common elements between the pages
- Can define a page from a python file or function
- The page is selected ins navigation must manually execute the page with the .run()
- [st.Page](http://st.Page)() → lets to define a page (python file or function)

```python
page = st.Page("pages/about.py", title="About", icon="ℹ️")

def home_page():
    st.write("Welcome to Home")
page = st.Page(home_page, title="Home")
```

- Allows to set label and title using *title* and *st.set_page_config()* can be used to change the page title and favicon
- Customizing navigation
    - using the *position* parameter, can display navigation menu in the sidebar or along the top of the apps
    - Can sort or group pages, as well as remove any pages

```python
nav = st.navigation([home_page, "pages/about.py"])
nav.run()

st.navigation({
    "Main": [home_page, about_page],
    "Additional": [help_page]
})  # nested inside of each other
```

## pages/ directory

- If pages/ directory is present next to the entrypoint file, streamlit will identify each python file within it as a Page
- Pages support run-on-save; A page modified while the app is running, and If user is on
    - the exact page → reruns
    - the different pages → will not automatically rerun
    

> All the pages share the **same session_state,** which allows to store and retrieve data across different pages
 

## st.switch_page()

- Used to programmatically move between the pages

```python
st.switch_page("pages/page_name.py")

# or, if it’s a page defined using st.Page()
st.switch_page("Page title")
```

- Navigate programmatically → for ex, After login

## st.page_link()

- Creates a clickable link that allows users to jump to another page without using the navigation menu
- Similar to Hyperlink
- User clicks manually → for ex, “Learn more”

> Navigation via Streamlit’s built-in tools keeps your app state.
Navigation via plain URLs or Markdown links resets it.
