<script lang="ts">
	import { onMount } from "svelte";
	import type { I18nFormatter } from "@gradio/utils";
	import WaveSurfer from "wavesurfer.js";
	import RecordPlugin from "wavesurfer.js/dist/plugins/record.js";

	export let recording = false;
	export let paused_recording = false;
	export let stop: () => void;
	export let record: () => void;
	export let waveform_settings = {};

	let micWaveform: WaveSurfer;
	let waveformRecord: RecordPlugin;

	onMount(() => {
		create_mic_waveform();
	});

	const create_mic_waveform = (): void => {
		if (micWaveform !== undefined) micWaveform.destroy();

		micWaveform = WaveSurfer.create({
			...waveform_settings,
			height: 100,
			container: "#microphone"
		});

		waveformRecord = micWaveform.registerPlugin(RecordPlugin.create());
	};
</script>

<div class="wrapper">
	<div id="microphone" style:display={recording ? "block" : "none"} />
	{#if recording}
		<button
			class="stop-button pulsate"
			on:click={() => {
				waveformRecord.stopMic();
				stop();
			}}
		>
			<div class="stop-icon">
				<img
				width="200"
				height="200"
				src="https://img.icons8.com/material-rounded/200/stop.png"
				alt="stop"
				/>
			</div>
		</button>
	{:else}
		<button
			class="record-button"
			on:click={() => {
				waveformRecord.startMic();
				record();
			}}
		>
			<div class="microphone-icon">
				<img
				width="200"
				height="200"
				src="https://img.icons8.com/material-rounded/200/microphone.png"
				alt="microphone"
				/>
			</div>
		</button>
	{/if}
</div>

<style>
	.wrapper {
		display: flex;
		align-items: center;
		justify-content: center;
		align-items: center;
		border-radius: 50px;
	}

	.microphone-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 100%;
	}

	.stop-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 100%;
	}

	.record-button {
		height: 350px;
		width: 350px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--button-secondary-background-fill);
	}

	.stop-button {
		height: 350px;
		width: 350px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--button-secondary-background-fill);
	}

	.record-button:hover {
        transform: scale(0.95);
	}

  @keyframes pulsate {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.1);
    }
    100% {
      transform: scale(1);
    }
  }

  .pulsate {
    animation: pulsate 1s infinite;
  }

	.record-button:disabled {
		cursor: not-allowed;
		opacity: 0.5;
	}

	@keyframes scaling {
		0% {
			background-color: var(--button-secondary-background-fill);
			scale: 1;
		}
		50% {
			background-color: var(--button-secondary-background-fill);
			scale: 1.2;
		}
		100% {
			background-color: var(--button-secondary-background-fill);
			scale: 1;
		}
	}
</style>
