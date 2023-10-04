<!--
Javascript - To declare and define the variable
-->
<script>
    let name = "Svelte"
    let img_src = '/image.gif';
</script>

<!--
To access in the markup
-->
<h2>Hello {name}!</h2>

<!-- 
To access the variable in a tag/element attribute 
-->
<img src={img_src} ... />

