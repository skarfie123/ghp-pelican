Title: Markdown
Date: 2023-03-19
Modified: 2023-06-01

For the source of this page, see: [GitHub](https://github.com/skarfie123/ghp-pelican/blob/master/content/markdown.md)

# H1

## H2

### H3

#### H4

##### H5

###### H6

- a
- b
- c

1. one
2. two
3. three

1\. is a great number. 

- spaced
  > list quote

- list

> > quote
> 
> this is a quote
> # something
>
> - blah
> - blah

`this is code`

```
this is a code block
```

indents also are a type of code block

    indented block

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

    #!/usr/bin/python
    print("Hello World!")

but

    :::python
    print("The triple-colon syntax will *not* show line numbers.")

highlight

    :::python hl_lines="1 3"
    # This line is emphasized
    # This line isn't
    # This line is emphasized

* * *

***

*****

- - -

---------------------------------------

This is [an example][id] reference-style link.

This is [an example](http://example.com/ "Title") inline link.

[id]: http://example.com/  "Optional Title Here"

Visit [Daring Fireball][] for more information.

[Daring Fireball]: http://daringfireball.net/

<http://example.com/>

<address@example.com>

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

~single tilde~

~~double tilde~~

![Alt text](./path/to/rss.png "Optional title")
![Alt text2](./images/rss.png "Optional title2")

Footnotes[^1] have a label[^@#$%] and the footnote's content.

[^1]: This is a footnote content.
[^@#$%]:
    A footnote on the label: "@#$%".

    It is still a number though.

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |