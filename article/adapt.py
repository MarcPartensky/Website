import re

def adapt(text, title, layout):
    text = correct_assets(text, layout)
    text = correct_title(text, title)
    text = add_icons(text)
    text = add_back_to_articles(text)
    # text = correct_links(text)
    # text = correct_scripts(text)
    text = add_mathjax(text)
    text = add_back_to_top_button(text)
    text = add_scroll_support(text)
    text = correct_check(text)
    text = add_load_static(text)
    # text = add_header(text)
    return text

def add_load_static_and_extends(text):
    """Add load static on top of the file."""
    return '{% extends "layout/home.html" %}\n\
            {% load static %}\n\
            {% block content %}\n' + text + \
           '{% endblock content %}'

def add_load_static(text):
    """Add load static on top of the file."""
    return '{% load static %}' + text

def add_header(text):
    header = """
  <header id="header" class="d-flex align-items-center">
    <div class="container">

      <!-- The main logo is shown in mobile version only. The centered nav-logo in nav menu is displayed in desktop view  -->
      <div class="logo d-block d-lg-none">
          <a data-aos="fade-down" href="/" class="icon-back-to-top"><img src="{% static 'home/assets/img/black-orchid.svg' %}" alt="" class="img-fluid"></a>
      </div>

      <nav class="nav-menu d-none d-lg-block">
        <ul class="nav-inner">
          <li class="active drop-down"><a href="">Sections</a>
            <ul>
              <li><a href="{% url 'touch-typing' %}">Touch typing</a></li>
              <li><a href="{% url 'calendar' %}">Calendar</a></li>
              <li><a href="{% url 'first-site' %}">First site</a></li>
              <li><a href="{% url 'game' %}">Games</a></li>
              <li><a href="{% url 'blog-home' %}">Blog</a></li>
              <li><a href="{% url 'cv' %}">Curriculum Vitae</a></li>
              <li class="drop-down"><a href="#">Projects</a>
                <ul>
                  <li><a href="#">Deep Drop Down 4</a></li>
                  <li><a href="#">Deep Drop Down 5</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="/#about">About me</a></li>
          <li><a href="/#skills">Skills</a></li>

          <li class="nav-logo" style="width: 15%; height: 15%"><a href="/"><img src="{% static 'home/assets/img/black-orchid.svg' %}" alt="" class="img-fluid"></a></li>

          <li><a href="/#portfolio">Portfolio</a></li>
          <li><a href="/#certificates">Certificates</a></li>
          <li><a href="/#contact">Contact</a></li>

        </ul>
      </nav><!-- .nav-menu -->

    </div>
    """
    text = text.replace('<div id="header">', header)
    return text

def add_back_to_articles(text):
    text = text.replace(
        '<div id="toc-inner">',
        '<div id="toc-inner">\n\
        <a class="back" class="container" href="{% url \'article\' %}"><p>Back to articles</p></a><div class="fade_rule"></div>')
    return text

def correct_title(text, title):
    """Put the true title."""
    pattern = re.compile(r'<title>(.*)</title>')
    wrong_title = re.findall(pattern, text)[0]
    text = text.replace(f"<title>{wrong_title}</title>",
                        f"<title>{title.capitalize()}</title>")
    return text


def add_icons(text):
    """Add orchid icons in tabs."""
    text = text.replace(
        '</title>',
        '</title>\n\
        <link href="{% static \'home/assets/img/white-orchid.svg\' %}" rel="icon">\n\
        <link href="{% static \'home/assets/img/black-orchid.svg\' %}" rel="apple-touch-icon">\n\
        <link href="{% static \'article/assets/css/main.css\' %}" rel="stylesheet">'
    )
    return text

def correct_links(text):
    """Correct import links."""
    pattern = re.compile(r'href=.assets\/(.*\.css)')
    for file in re.findall(pattern, text):
        print(file)
        text = text.replace(f'href="assets/{file}"',
                            'href="{% static \'article/assets/'+file+'\' %}"')
    return text

def correct_scripts(text):
    """Correct import scripts."""
    pattern = re.compile(r'src="assets\/(.*\.js)"')
    for file in re.findall(pattern, text):
        text = text.replace(
            '</body>',
            '<script src="{% static \'article/assets/'+file+'\' %}"></script>\n\
        </body>')
    return text

def correct_assets(text, layout):
    """Correct assets imports."""
    # pattern = re.compile(r'([src|href].?=.?[\'|"]assets\/.*\.[js|css].?[\'|"])')
    pattern = re.compile(r'(assets/.*\.[jc]ss?)')
    for match in re.findall(pattern, text):
        substitute = match.replace('assets', layout)
        substitute = "{% static 'article/"+substitute+"' %}"
        text = text.replace(match, substitute)
    return text


def add_mathjax(text):
    """Add mathjax support for latex formulaes rendering."""
    text = text.replace(
        "</head>",
        '<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>\n\
        </head>')
    return text

def add_scroll_support(text):
    """Add scroll support."""
    text = text.replace(
        '</body>',
        '<script src="{% static \'home/assets/vendor/jquery/jquery.min.js\' %}"></script>\n\
        <script src="{% static \'home/assets/vendor/waypoints/jquery.waypoints.min.js\' %}"></script>\n\
        <script src="{% static \'article/assets/js/main.js\' %}"></script>\n\
    </body>')
    return text

def correct_check(text):
    """Replace markdown check to checked buttons."""
    text = text.replace('[ ]', '<input type="checkbox" disabled="">')
    text = text.replace('[x]', '<input type="checkbox" disabled="" checked="">')
    return text

def add_back_to_top_button(text):
    """Add back to top button."""
    text = text.replace(
        '</body>',
        '</body>\n<a href="#" class="back-to-top" style="display: inline; \
        position:fixed; right:15px; bottom:15px; z-index:99999;"> \
        <i style="display: flex; align-items: center; justify-content: center; \
        font-size: 24px; width: 40px; height: 40px; border-radius: 4px; \
        background: #7cc576; color: #fff; transition: all 0.4s;" \
        class="icofont-simple-up"></i></a>')
    return text

