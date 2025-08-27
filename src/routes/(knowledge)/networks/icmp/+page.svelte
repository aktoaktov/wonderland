<script>
  import Section from "$lib/Markup/Section.svelte";
  import Title from "$lib/Elements/Title.svelte"
  import Par from "$lib/Markup/Par.svelte"
  import P from "$lib/Markup/P.svelte"
  import PackageBytes from "$lib/Demonstrtion/PackageBytes/PackageBytes.svelte"
  import PBPart from "$lib/Demonstrtion/PackageBytes/PBPart.svelte"
</script>

<Title title="Протокол ICMP"
/>

<Section>
  <Par>
    <P>
      ICMP (Internet control message protocol) &mdash; сетевой протокол, предназначенный для передачи сообщений об
      ошибках и других исключительных ситуаций. По протоколу ICMP также работает утилита ping.
    </P>
  </Par>

  <Par>
    <P>ICMP-пакет содержится внутри IP-пакета, состоит из заголовка и данных. Весь пакет имеет формат</P>
  </Par>

  <PackageBytes>
    <PBPart length="8"><b>Type</b></PBPart>
    <PBPart length="8"><b>Code</b></PBPart>
    <PBPart length="16"><b>Checksum</b></PBPart>
    <PBPart big length="32" realLength="16"><b>Rest of header</b></PBPart>
    <PBPart upto length="65535" bytes realLength="16"><b>Data</b>, формат зависит от значений Type и Code</PBPart>
  </PackageBytes>
</Section>