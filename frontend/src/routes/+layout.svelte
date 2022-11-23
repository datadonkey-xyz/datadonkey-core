<script lang="ts">
  import "carbon-components-svelte/css/white.css";
  import "../app.sass";
  import { MathQuillSetup } from 'svelte-mathquill';
  import { Content, Header, HeaderAction, HeaderNav, HeaderNavItem, HeaderPanelDivider, HeaderPanelLink, HeaderPanelLinks, HeaderUtilities, Modal, SideNav, SideNavItems, SideNavLink, SideNavMenu, SideNavMenuItem, SkipToContent } from "carbon-components-svelte";
  import { InformationFilled } from "carbon-icons-svelte";
  import { goto } from "$app/navigation";
  import { page } from "$app/stores";
  import navItems from "$lib/nav";

  let sidenavOpen = false;

</script>

<MathQuillSetup/>

<Header company="DataDonkey" platformName="Lab Tools" bind:isSideNavOpen={sidenavOpen} expandedByDefault={true}>
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
  <HeaderNav>
    <HeaderNavItem isSelected={$page.url.pathname == "/"} href="/" text="Home"/>
    <HeaderNavItem isSelected={
      $page.url.pathname == '/imaging' || /^\/imaging\/.*$/.test($page.url.pathname)
    } href="/imaging" text="Imaging"/>
    <HeaderNavItem isSelected={
      $page.url.pathname == '/data' || /^\/data\/.*$/.test($page.url.pathname)
    } href="/data" text="Data Analysis"/>
  </HeaderNav>
  <HeaderUtilities>
    <HeaderAction icon={InformationFilled} closeIcon={InformationFilled} text="About">
    <HeaderPanelDivider>Information Links</HeaderPanelDivider>
    <HeaderPanelLinks>
      <HeaderPanelLink href="https://datadonkey.xyz" target="_blank">DataDonkey Homepage</HeaderPanelLink>
      <HeaderPanelLink href="https://git.turtlebasket.ml/datadonkey-com" target="_blank">DataDonkey Git Repos</HeaderPanelLink>
      <HeaderPanelLink href="https://git.turtlebasket.ml/datadonkey-com/proto" target="_blank">Lab Tools Source Code</HeaderPanelLink>
    </HeaderPanelLinks>
    </HeaderAction>
  </HeaderUtilities>
</Header>

{#if $page.url.pathname != "/"}
<SideNav bind:isOpen={sidenavOpen}>
  <SideNavItems>
    {#each Object.keys(navItems) as navType}
      {#if $page.url.pathname == `/${navType}` || (new RegExp(`^\/${navType}\/.*$`)).test($page.url.pathname)}
        {#each navItems[navType].sort((a, b) => {
          if (a.name > b.name) {
            return 1
          } 
          else {
            return -1
          }
        }) as navItem}
        <SideNavLink text={`${navItem.name}`} href={`/imaging/${navItem.urlPath}`} isSelected={
          $page.url.pathname == `/imaging/${navItem.urlPath}`
        }/>
        {/each}
      {/if}
    {/each}
  </SideNavItems>
</SideNav>
{/if}

<Content>
  <slot/>
</Content>
