# credit_scroll

Use moviepy to create scrolling video credits.

# Example

```python
import credit_scroll

title = [
    'My Movie',
    'This is centered',
    '',
    ('Two columns', 'Outer justified'),
    '',
    'This can be as long as you like',
    'with one line per line in the credits',
    '',
    ('Multiple lines in right column?', 'Sure'),
    ('',                                'Why not?'),
]


credit_scroll.writeCredits(title, 'hello.mp4')

```