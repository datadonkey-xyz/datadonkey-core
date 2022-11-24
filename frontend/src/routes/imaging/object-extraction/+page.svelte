<script>

	import { InlineNotification } from "carbon-components-svelte";
import { ImageSearchAlt } from "carbon-icons-svelte";

</script>
<div class="title-row">
  <ImageSearchAlt size={32}/>
  <h1>Object Extraction</h1>
</div>
<br>
<p>Detects and extracts objects in the image. Uses a simple, 
  contrast-based edge detection strategy.</p>
<br>

<InlineNotification
  hideCloseButton
  lowContrast
  kind="warning"
  title="This feature is currently under construction."
  subtitle="Check again soon!"
/>
