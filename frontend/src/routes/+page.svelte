<script>
	import { goto } from "$app/navigation";
	import { ClickableTile, Column, Grid, Row} from "carbon-components-svelte";
	import { Fire, FunctionMath, WatsonHealthSmoothing } from "carbon-icons-svelte";

</script>
<h1>Lab Tools</h1>
<br>
<p>A collection of useful utilities for image & data processing work. 
  Built with ❤️ by DataDonkey, and fully open-source.</p>
<br>
<br>

<h3>Popular Workflows</h3>
<br>

<Grid noGutter padding={true}>
  <Row>
    <Column>
      <ClickableTile href="/imaging/math-transform">
        <div class="tile-row">
          <FunctionMath size={32}/>
          <div class="tile-col">
            <h4>Mathematical Transform</h4>
            <p>Transforms an image using a LaTeX-formatted math formula.</p>
          </div>
        </div>
      </ClickableTile>
    </Column>
    <Column>
      <ClickableTile href="/imaging/heatmap">
        <div class="tile-row">
          <Fire size={32}/>
          <div class="tile-col">
            <h4>Heatmap</h4>
            <p>Generates a heatmap of pixel intensities.</p>
          </div>
        </div>
      </ClickableTile>
    </Column>
  </Row>
  <Row>
    <Column>
      <ClickableTile href="/imaging/smooth-conv">
        <div class="tile-row">
          <WatsonHealthSmoothing size={32}/>
          <div class="tile-col">
            <h4>Convolutional Smooth</h4>
            <p>Applies a smoothing kernel to an image.</p>
          </div>
        </div>
      </ClickableTile>
    </Column>
    <Column>
      <ClickableTile href="/imaging/heatmap">
        <div class="tile-row">
          <Fire size={32}/>
          <div class="tile-col">
            <h4>Heatmap</h4>
            <p>Generates a heatmap of pixel intensities.</p>
          </div>
        </div>
      </ClickableTile>
    </Column>
  </Row>
</Grid>