# Svelte - Components

## Variables and Texts
### Initialization, Definition and Declaration
- To initialize a variable
    + Use the 'let' keyword (Javascript basics)
    ```javascript
    <script>
        let variable_name = 'value';
    </script>
    ```

- To access a variable from the markup
    + Use the '{variable-name}' special keyword/character in the markup
    ```console
    <h1>{variable_name}</h1>
    ```

- To format the variable to Upper case
    + Format the variable with '[variable-name].toUpperCase()' function
    ```html
    <h1>{variable_name.toUpperCase()}</h1>
    ```

## Dynamic Attributes
### Controlling Element Attributes
+ Just like you can use curly braces to control text, you can use them to control element attributes.
- Using variable in a tag/element attribute
    - Image
        - Define variable
            ```javascript
            <script>
                let src = '/image.gif';
            </script>
            ```
        - Reference
            ```html
            <img src={src} [other-attributes ...] />
            ```

## Resources

## References
+ [Svelte Learn - Tutorial - your first component](https://learn.svelte.dev/tutorial/your-first-component)

## Remarks