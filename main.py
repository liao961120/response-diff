IN = "data.txt"
OUT = "index.html"

import colorsys

def main():
    lines = ""
    for line in load_data_file(IN):
        lines += wrap_p(wrap_span(line))
    lines = wrap_div(lines)

    html = html_maker(title=IN, lines=lines)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)


def load_data_file(fp):
    with open(fp) as f:
        return [l for l in f]

def wrap_div(s: str):
    return f'<div>{s}</div>'

def wrap_p(s: str):
    return f'<p>{s}</p>'

def wrap_span(s: str):
    def filt(s):
        if s == " ": return "BLANK"
        if s == "?": return "QUESTION"
        return s
    def filt2(s):
        if s == " ": return "&nbsp;"
        return s
    return ''.join(f'<span title="{i+1}" class="_{filt(c)}">{filt2(c)}</span>' for i, c in enumerate(s))

def class_style_maker(cls_names):
    style = ""
    cls_names = [x for x in cls_names if x.strip() != '']
    colors = style_colors(len(cls_names))
    for cls, color in zip(cls_names, colors):
        style += f'span.{cls} ' + '{' + f'color:{color};' + '}\n'
    return style

def style_colors(N=10):
    HSV_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        hex_out.append('#%02x%02x%02x' % tuple(rgb))
    return hex_out


def html_maker(title, lines):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
            {lines}
        <style>
            {general}
        </style>
        <link rel="stylesheet" href="styles.css">
        
    </body>
    </html>
    '''
    general = '''
    body { 
        overflow-x: auto;
        width: fit-content;
    }
    p:nth-child(odd) {
        background-color: rgba(200, 200, 200, 0.1);
    }
    div > p:hover {
        background-color: rgba(175, 175, 175, 0.3);
    }
    div > p:hover:before {
        color: red;
        font-weight: bold;
    }
    p { 
        white-space: nowrap;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        margin: 0;
        padding: 0;
        line-height: 1.1;
        font-size: 19px;
        counter-increment: line;
    }
    p:before {
        content: counter(line);
        border-right: 1px solid #ddd;
        margin-right: .5em;
        color: #888;
        width: 1.8em;
        display: inline-block;
        text-align: right;
        font-size: 0.8em;
        font-weight: normal;

        position: sticky;
        left: 0;
        background: white;
        padding: .21em .5em;
    }
    div > p > span {
        cursor: pointer;
        border: 1px transparent solid;
    }
    div > p > span:hover {
        border: 1px black solid;
    }
    ._A {background-color: #00486a; color: white;}
    ._B {background-color: #ffa600; color:white}
    ._C {background-color: #bc5090; color:white}
    ._D {background-color: #ff6361; color:white}
    ._E {color: #00486a;}
    ._F {color: #bc5090;}
    ._G {color: #ffa600;}
    ._H {color: #ff6361;}
    ._BLANK {
        border: 1px grey dotted;
    }
    ._QUESTION {
        color: #58508d; 
        border: 1px grey dotted;
    }
    ._Y {text-decoration: underline; }
    ._N {
        color: white;
        background: black;
    }
    ._P {color: blue;}
    ._X {color: red;}
    '''
    return html.format(title=title, lines=lines, general=general)


if __name__ == '__main__':
    main()
