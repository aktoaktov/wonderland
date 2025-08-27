<script>
import Title from "$lib/Elements/Title.svelte"
import Par from "$lib/Markup/Par.svelte"
import P from "$lib/Markup/P.svelte"
import Codeblock from "$lib/Code/Codeblock.svelte"
</script>

<Title title="Абстрактные таблицы"
/>

<Par>
    <P>
        Большие наборы записей и скалярных типах нужно как-то хранить.

    </P>
    <P>
        Записью всегда выступает тип (возможно, комплексный), описание которого мы заранее знаем полностью.
        Например, если мы делаем сервис для доставки еды, и нам нужно хранить пользователей, то для них мы сделаем запись
    </P>
</Par>

<Codeblock code={
`record User:
    string name
    int age
    string address`
}/>