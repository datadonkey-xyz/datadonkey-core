<script lang="ts">
	import { Button, FormLabel } from "carbon-components-svelte";
	import { Checkmark, Fire, Save } from "carbon-icons-svelte";
	import SelectFileSingle from "src/components/SelectFileSingle.svelte";

  let files: File[] = [];

  let loading = false;
  let finished = false;
</script>

<div class="title-row">
  <Fire size={32}/>
  <h1>Pixel Intensity Heatmap</h1>
</div>
<br>
<p>Generates a heatmap based on pixel intensities.</p>
<br>

<SelectFileSingle
type="image"
bind:files
/>
<br>

<Button on:click={() => {}} icon={Checkmark}>Apply Transformation</Button>
<Button on:click={() => {}} icon={Save} kind="secondary" disabled={!finished}>Save Output</Button>
