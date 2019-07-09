---
layout: post
title: Sublime Snippets
tags: programming tools
---

I often write code using Sublime. Today, I was writing a script in Python and scaffolding out the different functions I thought that I would need, using the `pass` keyword as a placeholder for the body of each of the functions. A habit that I have (maybe a bad one) is to leave the comment `# todo` to mark places where I need to make changes. This could be actually filling in an implementation, removing placeholder code, or any other sort of change. Today, one `# todo` was for refining a constant value, others were for placeholder data, etc. I realized that there was probably a way to make it so that when I typed `pass` Sublime would autocomplete (or I could tab-complete) to `pass # todo`.

First, I looked up plugins for Sublime, but that wasn't quite what I was looking for. Then, I came across [snippets](http://docs.sublimetext.info/en/latest/extensibility/snippets.html). What I wanted is the following simple code

~~~~
<snippet>
    <content><![CDATA[
pass # todo
]]></content>
    <tabTrigger>pass</tabTrigger>
    <scope>source.python</scope>
</snippet>
~~~~

I came across [this post](https://webdevstudios.com/2016/08/16/snippets-saved-life-how-sublime-text-3-snippets-changed-everything/) which has made me want to further customize my programming environment. I'm going to store my changes to my Sublime environment [here](https://github.com/agdenadel/sublime-customization).