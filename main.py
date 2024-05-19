import flet as ft
from flet import TextField, Text, Row, MainAxisAlignment, CrossAxisAlignment, Page, AppBar

def main(page: Page):
    page.title = "MD Mojo"
    page.theme_mode = "light"
    
        
    def update_preview(e: ft.ControlEvent):
        md.value = text_field.value
        page.update()
    
    page.appbar = AppBar(title=Text("MD Mojo", color="white", size=20, weight="bold"),
                         center_title=True,
                         bgcolor="black",
                         elevation=0)
    
    text_field = TextField(value='''# Title

## Subtitle

### Sub-subtitle

#### Sub-sub-subtitle

---

**Bold Text**

*Italic Text*

[Link](https://example.com)

- List item 1
- List item 2
  - Sub-item A
  - Sub-item B

1. Numbered item 1
2. Numbered item 2
   - Sub-item X
   - Sub-item Y

> Blockquote

`Inline code`

```python
# Code block
print("Hello, world!")
''', multiline=True, expand=True, border_color=ft.colors.TRANSPARENT, on_change=update_preview)
    
    md = ft.Markdown(value=text_field.value, selectable=True, extension_set="gitHubWeb", on_tap_link=lambda e: page.launch_url(e.data))
    
    page.add(
        Row(
            controls=[
                text_field,
                ft.VerticalDivider(color=ft.colors.AMBER),
                ft.Container(
                    ft.Column(
                        [md],
                        scroll="hidden",
                    ),
                    expand=True,
                    alignment=ft.alignment.top_left
                )
            ],
            vertical_alignment=CrossAxisAlignment.START,
            expand=True,
        )
    )
    
    

if __name__ == '__main__':
    ft.app(target=main)