<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
    import Section from "$lib/Markup/Section.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Гомоморфизм"
/>
<Section>
<Par>
    <P>
        <b>Гомоморфизм</b> группы <Math m="G"/> в <Math m="H"/> --
        отображение <Math m="\phi \colon G \to H"/>, сохраняющее групповую
        структуру
    </P>
    <Math display m="\phi(a * b) = \phi(a) \cdot \phi(b)"/>
</Par>

<Par>
    <P>
        <b>Образ</b> гомоморфизма{" "}
        <Math
                m={`\\im \\phi \\defeq \\{\\phi(g) \\mid \\weak{\\forall g \\in G}\\}`}
        />
        ,<Math m="\im \phi"/> -- подгруппа в <Math m="H"/>.
    </P>
    <P>
        <b>Ядро</b> гомоморфизма{" "}
        <Math
                m={`\\ker \\phi \\defeq \\{g \\in G \\colon \\phi(g) = 1\\}`}
        />{" "}
        -- все элементы
        <Math m="G"/>, отображающиеся в <Math m="1"/>.<br/>
        <Math m="\ker \phi"/> -- нормальная подгруппа в <Math m="G"/>.
    </P>
</Par>

<Par>
    <P>
        <b>Мономорфизм</b> -- инъективным гомоморфизм,{" "}
        <Math m="\ker \phi = 1"/>
    </P>
    <P>
        <b>Эпиморфизм</b> -- сюръективный гомоморфизм,{" "}
        <Math m="\im \phi = G"/>
    </P>
    <P>
        <b>Эндоморфизм</b> -- гомоморфизм на себя (гомоморфизм{" "}
        <Math m="G \to G"/>)
    </P>
</Par>

<Par>
    <P>
        Если <Math m="{`H <| G`}"/>, то <Math m="H"/> -- ядро гомоморфизма{" "}
        <Math m="\kappa \colon G \to G/H"/>
        <br/>
        <Math m="\kappa"/> называется <b>каноническим гомоморфизмом</b> или
        канонической проекцией на факторгруппу.
    </P>
    <Math display m="\kappa(g) = g \cdot H"/>
</Par>

<Par>
    <P>
        <em>Основная теорема о гомоморфизмах</em>
        Пусть <Math m="\phi"/> -- гомоморфизм группы <Math m="G"/> в{" "}
        <Math m="H"/>. Тогда
    </P>
    <Math display m="G / \ker \phi \isom \im \phi"/>
</Par>
<Proof>
    <Par>
        <P>
            <em>Лемма</em> Прообразы элементов группы <Math m="H"/> при
            гомоморфизме <Math m="\phi"/> -- это то же самое, что и смежные
            классы по ядру гомоморфизма <Math m="\ker \phi"/>
        </P>
        <Math display m={`\\weak{h \\in \\im \\phi} \\quad h = \\phi(g) => \\phi^{-1}(h) = g * \\ker \\phi`}/>
        <P>
            Доказательство. Пусть какой-то элемент <Math m="g' = g * k"/>{" "}
            лежит в прообразе элемента <Math m="h"/>. Тогда
        </P>
        <Math display
              m="{`\\phi(g') = \\phi(g * k) = \\phi(g) \\cdot \\phi(k) = h \\cdot \\phi(k) = h ~<==>~ \\phi(k) = 1 ~<=>~ k \\in \\ker \\phi`}"/>
        <P>
            Получаем, что элементы из прообраза <Math m="h"/> -- это элементы
            из <Math m="g * \ker \phi"/>.
        </P>
    </Par>
    <Par>
        <P>
            Группа <Math m="G"/> &laquo;расслаивается&raquo; на смежные
            классы, которым соответствуют точкам из образа <Math m="\phi"/>.
            Отсюда следует существование биекции{" "}
            <Math m="{`\\psi \\colon G / \\ker \\phi <-> \\im \\phi`}"/>{" "}
            такой, что
            <Math m="\phi(g) = \psi(g * \ker \phi)"/>.
        </P>
        <P>
            А <Math m="\psi"/> -- гомоморфизм,{" "}
            <Math m="\psi(g * g' * \ker \phi) = \phi(g * g') = \phi(g) \cdot \phi(g')
                = \psi(g*\ker \phi) \cdot \psi(g'*\ker\phi)"/>
            . Значит, <Math m="\psi"/> -- изоморфизм.
        </P>
    </Par>
</Proof>
</Section>

<Section>
<Heading>Автоморфизмы</Heading>

<Par>
    <P>
        <b>Автоморфизм</b> -- изоморфизм группы на себя.
    </P>
    <P>
        Автоморфизмом является обратимый эндоморфизм, а так же изоморфизм
        группы на себя.
    </P>
</Par>

<Par>
    <P>
        <b>Группа автоморфизмов</b>
        <Math m="\Aut G"/> -- множество всех автоморфизмов группы с
        операцией композиции.
    </P>
    <P>
        <Math m="\Aut G"/> -- инвариант группы. Например, если{" "}
        <Math m="\Aut G \nisom \Aut H"/>, то <Math m="G \nisom H"/>
    </P>
    <P>
        <Math m="\Aut G"/> -- подгруппа в группе перестановок{" "}
        <Math m="\S(G)"/>.
    </P>
</Par>

<Subheading>Примеры групп автоморфизмов</Subheading>
<Par>
    <P>
        Циклические группы
        <br/>
        <Math m="{`\\Aut \\C_\\oo = \\{\\pm 1\\}`}"/>
        <br/>
        <Math
                m={`\\Aut \\C_n \\isom \\ZZ_n^\\times = \\{k \\colon \\gcd(n, k) = 1 \\}`}
        />{" "}
        -- все обратимые по модулю <Math m="n"/>.
    </P>
</Par>

<Subheading>Внутренние автоморфизмы</Subheading>
<Par>
    <P>
        <b>Внутренний автоморфизм</b>, определенный элементом <Math m="g"/>{" "}
        -- автоморфизм{" "}
        <Math m="{`\\phi_g(x) = g \\cdot x \\cdot g^{-1}`}"/>
    </P>
    <P>
        Произвольному элементу <Math m="g \in G"/> сопоставим внутренний
        автоморфизм <Math m="\phi_g"/>. Получили отображение{" "}
        <Math m="{`\\phi \\colon G -> \\Aut G,~ g |-> \\phi_g`}"/>,
        являющиеся гомоморфизмом группы <Math m="G"/> в <Math m="\Aut G"/>
        .
    </P>
    <P>
        Ядро этого гомоморфизма <Math m="\ker \phi"/> -- группа из таких
        элементов в <Math m="G"/>, для которых <Math m="\phi_g(x) = x"/>,
        то есть элементы, коммутирующие со всеми. Значит,{" "}
        <Math m="\ker \phi = \Z(G)"/>.
    </P>
</Par>
<Par>
    <P>
        <b>Группа внутренних автоморфизмов</b>
        <Math m="\Inn G \defeq \im \phi \isom G/\Z(G)"/>
    </P>
    <P>
        <em>Лемма</em>
        <Math m="{`\\Inn G <| \\Aut G`}"/>
    </P>
    <Proof>
        <P>
            Подгруппа нормальна, если вместе с каким-то элементом она содержит
            и все его сопряженные.
        </P>
        <P>
            Проверим, что <Math m="\forall\, \phi_g \in \Inn G"/> и{" "}
            <Math m="\forall\, \psi \in \Aut G"/> элемент{" "}
            <Math m="\psi \compose \phi_g \compose \psi^-1 \in \Inn G"/>.
        </P>
        <Math display m="
              \bl(\psi \compose \phi_g \compose \psi^-1\br)(x) = \psi\b(g \cdot
              \psi^-1(x) \cdot g^-1\b) = \psi(g) \cdot x \cdot \psi(g)^-1
            "/>
        <P>
            А это сопряжение с <Math m="\psi(g)"/>, то есть элемент{" "}
            <Math m="\Inn G"/>
        </P>
        <Math m={`\\psi \\compose \\phi_g \\compose \\psi^-1 = \\phi_{\\psi(g)}`}/>
    </Proof>
</Par>

<Subheading>Внешние автоморфизмы</Subheading>
<Par>
    <P>
        <b>Внешний автоморфизм</b> -- автоморфизм, но не внутренний
    </P>
    <P>
        <b>Группа внутренних автоморфизмов</b>
        <Math m="\Out G \defeq \Aut G / \Inn G"/> -- группа, состоящая из
        смежных классов всех автоморфизмов по внутренним
    </P>
</Par>

<Subheading>Автоморфизмы, сохраняющие классы</Subheading>
<Par>
    <P>
        <b>Автоморфизм класса</b> -- автоморфизм, который переводит элемент
        в пределах его класса сопряженности. Это автоморфизм{" "}
        <Math m="\phi"/>, что для любого <Math m="g"/> существует{" "}
        <Math m="h"/> такой, что{" "}
        <Math m="\phi(g) = h \cdot g \cdot h^-1"/>.
    </P>
    <P>
        <b>Группа автоморфизмов класса</b>
        <Math m="\CPAut G"/> -- группа, состоящая из всех автоморфизмов
        класса
    </P>
</Par>
</Section>
