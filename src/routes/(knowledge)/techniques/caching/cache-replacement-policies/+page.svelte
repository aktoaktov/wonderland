<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
</script>

<Title title="Алгоритмы вытеснения кеша"
/>

<Par>
    <P>
        Когда кеш заполнен, система должна решить, какие данные удалить, чтобы освободить место для новых.
        Для этого используются различные алгоритмы вытеснения, каждый из которых имеет свои преимущества и недостатки.
    </P>
</Par>


<Heading>LRU &mdash; Least Recently Used</Heading>

<Par>
    <P>
        При политике LRU вытесняется элемент, к которому дольше всего не обращались.
    </P>
</Par>