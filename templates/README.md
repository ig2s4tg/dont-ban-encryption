This folder holds templates for the pages of your site. These are written in Jinja2, a templating language, which is like HTML but it can do more, like “extend” other files. A common way to do this is have a “base” file, in which you include things that all the pages will have in common, like navigation bars or footers, so that you don’t have to write them for every single page.

This templating language also allows you to do python-y stuff within the template, which is great for things like:

```
if user is logged in:
   <div>logged in</div>
else:
   <div>not logged in</div>
```
