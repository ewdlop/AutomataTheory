# AutomataTheory

## Regular language

```markdown
If you need a **regex pattern that matches alphabets including accented characters**, you can use the following pattern:
```
```regex
[\p{L}\p{M}]+
```

### Explanation:
```markdown
- `\p{L}`: Matches any Unicode letter, including accented characters.
- `\p{M}`: Matches diacritical marks (for combining accents).
- `+`: Ensures it matches one or more characters.
```

### Example Matches:
```markdown
- **Café**
- **résumé**
- **naïve**
- **français**
- **Schrödinger**
```
```markdown
If your regex engine **does not support Unicode properties (`\p{L}` and `\p{M}`)**, you can use a broader character set:
```
```regex
[a-zA-ZÀ-ÖØ-öø-ÿ]+
```
```markdown
This explicitly includes:
- `À-Ö`: Uppercase accented letters
- `Ø-ö`: More accented characters
- `ø-ÿ`: Lowercase accented letters

Would you like this pattern for a specific programming language?
```
