<script lang="ts">
	import { Button, FormLabel, Slider, TextInput } from "carbon-components-svelte";
	import { Checkmark, Save, WatsonHealthSmoothing } from "carbon-icons-svelte";
	import SelectFileSingle from "src/components/SelectFileSingle.svelte";

  let files: File[] = [];
  let radius: number = 1;

  let loading = false;
  let finished = false;

</script>

<div class="title-row">
  <WatsonHealthSmoothing size={32}/>
  <h1>Convolutional Smoothing</h1>
</div>
<br>
<p>Applies a convolutional smoothing kernel of a customizable radius.</p>
<br>

<SelectFileSingle
type="image"
bind:files
/>
<br>

<div class="form">
<FormLabel>Smoothing Radius (px)</FormLabel>
<Slider bind:value={radius} min={1} max={40}/>
<br>
</div>

<Button on:click={() => {}} icon={Checkmark}>Apply Transformation</Button>
<Button on:click={() => {}} icon={Save} kind="secondary" disabled={!finished}>Save Output</Button>
