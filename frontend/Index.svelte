<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { DateInput } from 'date-picker-svelte';

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: string | null = null;
	export let date_value = new Date();
	export let value_is_output = false;

	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		change: never;
		input: never;
	}>;

	async function handleChange() {
		value = date_value.toISOString().split('T')[0];
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
		}
	}

	$: date_value, handleChange()
	$: if(value) {
		date_value = new Date(value);
	}


</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
	/>

	<div>"Hello"</div>

	<DateInput bind:value={date_value}></DateInput>

</Block>
