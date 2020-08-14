Title: Building a blog site
Date: 2020-08-14 12:00
Modified: 2020-08-14 12:00
Category: web-design
Tags: tech, writing, web-design
Slug: building-the-blog
Summary: Design decisions, and setting up an environment so that I can "just write."

## A Website to Call My Own

I wanted a simple, clean design setup that was both accessible and reasonably nice looking on as many devices as possible.

  - The site needed to be able to handle showing code blocks and $\LaTeX$ markup.
    - Preferrably something with a highlighter for code blocks and embeddable mathjax support
  - The design should be minimalist, leaning on brutalist
    - Minimize code footprint by minimizing usage of javascript, fontawesome, css frameworks, etc
    - As much control of the design as possible (no commercial CMS - Wordpress, Wix, Squarespace, etc)
  - Writing and updating pages should be simple
    - WYSIWYG editors can be a pain for inserting high quality code blocks and math
  - Works within a toolchain that I'm used to
    - I'm used to working with $\LaTeX$ in a text editor
    - I'm familiar with reStructuredText and markdown formats
    - I'm comfortable with Git, Python, & the SysAdmin/DevOps components of a single server deployment
      - I don't need the weight of Django or Flask

These requirements really narrowed down how I would be able to serve my website; and after doing some digging, the best setup for all of this with the most minimal learning curve was going to be doing a python based, static site generator that serves the site through Github Pages.  I'd narrowed it down to Pelican & Nikola, and while Nikola looks like it may be more extensible, I went with Pelican due to familiarity with their templating engine.

### Using Pelican

Building out the custom HTML templating and css was the biggest portion of work; along with learning about configuration of Pelican.

### Using Github Pages

I'm apparently an idiot, and this was harder than any other peices of implementation... even though the instructions for creating a GitHub user page are clear, and it's extremely obvious in the Pelican docs that I'm syncing the output folder with the git repository that I create called <user>.github.io.

### Using Markdown

Whee Markdown, it's easy, consistant, and light weight; if I get squirly I may switch over to ReStructuredText but I'm lazy, and Markdown meets most of my use cases.

### Other Stuff

There's other things too, but I'm working on combatting some personal tendancies about "not publishing anything until it's perfect."  So, I guess it's time to hit publish.  I'll maybe write a part two about accessibility and responsive design.
