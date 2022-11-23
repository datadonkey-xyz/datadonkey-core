<script lang="ts">
	import { Button, Checkbox, FileUploaderButton, FormLabel, Select, SelectItem, SelectItemGroup, StructuredList, StructuredListBody, StructuredListCell, StructuredListHead, StructuredListRow } from "carbon-components-svelte";
	import { Checkmark, FunctionMath, Group, Label, Save } from "carbon-icons-svelte";
	import SelectFileSingle from "src/components/SelectFileSingle.svelte";
  import { MathQuill } from "svelte-mathquill";

  // inputs
  let files: File[] = [];
  let latex: string = "";

  // options
  let autoMinMax = true;
  let heatmapOutput = true;

  // state
  let loading = false;
  let finished = false;
</script>

<div class="title-row">
  <FunctionMath size={32}/>
  <h1>Mathematical Transform</h1>
</div>
<br>
<p>Applies a mathematical operation to every pixel in the image.</p>
<br>

<SelectFileSingle
type="image"
bind:files
/>
<br>

<FormLabel>Enter Transform Formula:</FormLabel><br>
<MathQuill bind:latex class="mathquill"/>
<br><br>

<!-- Legend -->
<div class="image-math-legend-table">
<StructuredList condensed>
  <StructuredListHead>
    <StructuredListRow head>
      <StructuredListCell head>Variable</StructuredListCell>
      <StructuredListCell head>Value</StructuredListCell>
      <StructuredListCell head>Description</StructuredListCell>
    </StructuredListRow>
  </StructuredListHead>
  <StructuredListBody>
    <StructuredListRow>
      <StructuredListCell><strong>R</strong></StructuredListCell>
      <StructuredListCell>0 to 255</StructuredListCell>
      <StructuredListCell>Pixel Red Intensity</StructuredListCell>
    </StructuredListRow>
    <StructuredListRow>
      <StructuredListCell><strong>G</strong></StructuredListCell>
      <StructuredListCell>0 to 255</StructuredListCell>
      <StructuredListCell>Pixel Green Intensity</StructuredListCell>
    </StructuredListRow>
    <StructuredListRow>
      <StructuredListCell><strong>B</strong></StructuredListCell>
      <StructuredListCell>0 to 255</StructuredListCell>
      <StructuredListCell>Pixel Blue Intensity</StructuredListCell>
    </StructuredListRow>
    <StructuredListRow>
      <StructuredListCell><strong>A</strong></StructuredListCell>
      <StructuredListCell>0 to 255</StructuredListCell>
      <StructuredListCell>Pixel Alpha Intensity (optional)</StructuredListCell>
    </StructuredListRow>
  </StructuredListBody>
</StructuredList>
</div>

<Checkbox labelText="Automatically calculate intensity maxima & minima" bind:checked={autoMinMax}/>
<Checkbox labelText="Ouptut a heatmap" bind:checked={heatmapOutput}/>
<br>

<Button on:click={() => {}} icon={Checkmark}>Apply Transformation</Button>
<Button on:click={() => {}} icon={Save} kind="secondary" disabled={!finished}>Save Output</Button>
