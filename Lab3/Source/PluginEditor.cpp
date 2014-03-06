/*
  ==============================================================================

    This file was auto-generated by the Introjucer!

    It contains the basic startup code for a Juce application.

  ==============================================================================
*/

#include "PluginProcessor.h"
#include "PluginEditor.h"


//==============================================================================
FilterAudioProcessorEditor::FilterAudioProcessorEditor (FilterAudioProcessor* ownerFilter)
    : AudioProcessorEditor (ownerFilter),
	infoLabel(String::empty),
	gainLabel("", "Throughput level:"),
	delayLabel("", "Delay:"),
	gainSlider("gain"),
	delaySlider("delay")
{
		// add some sliders..
		addAndMakeVisible(gainSlider);
		gainSlider.setSliderStyle(Slider::Rotary);
		gainSlider.addListener(this);
		gainSlider.setRange(0.0, 1.0, 0.01);

		addAndMakeVisible(delaySlider);
		delaySlider.setSliderStyle(Slider::Rotary);
		delaySlider.addListener(this);
		delaySlider.setRange(0.0, 1.0, 0.01);

		// add some labels for the sliders..
		gainLabel.attachToComponent(&gainSlider, false);
		gainLabel.setFont(Font(11.0f));

		delayLabel.attachToComponent(&delaySlider, false);
		delayLabel.setFont(Font(11.0f));

		// add the midi keyboard component..
		//addAndMakeVisible(midiKeyboard);

		// add a label that will display the current timecode and status..
		addAndMakeVisible(infoLabel);
		infoLabel.setColour(Label::textColourId, Colours::blue);

		// add the triangular resizer component for the bottom-right of the UI
		addAndMakeVisible(resizer = new ResizableCornerComponent(this, &resizeLimits));
		resizeLimits.setSizeLimits(150, 150, 800, 300);

    // This is where our plugin's editor size is set.
    setSize (400, 300);
}

FilterAudioProcessorEditor::~FilterAudioProcessorEditor()
{
}

//==============================================================================
void FilterAudioProcessorEditor::paint (Graphics& g)
{
    g.fillAll (Colours::white);
    g.setColour (Colours::black);
    g.setFont (15.0f);
    g.drawFittedText ("Hello World!",
                      0, 0, getWidth(), getHeight(),
                      Justification::centred, 1);
}

void FilterAudioProcessorEditor::resized()
{
	infoLabel.setBounds(10, 4, 400, 25);
	gainSlider.setBounds(20, 60, 150, 40);
	delaySlider.setBounds(200, 60, 150, 40);

	//const int keyboardHeight = 70;
	//midiKeyboard.setBounds(4, getHeight() - keyboardHeight - 4, getWidth() - 8, keyboardHeight);

	resizer->setBounds(getWidth() - 16, getHeight() - 16, 16, 16);

	getProcessor()->lastUIWidth = getWidth();
	getProcessor()->lastUIHeight = getHeight();
}

//==============================================================================
// This timer periodically checks whether any of the filter's parameters have changed...
void FilterAudioProcessorEditor::timerCallback()
{
	FilterAudioProcessor* ourProcessor = getProcessor();

	AudioPlayHead::CurrentPositionInfo newPos(ourProcessor->lastPosInfo);

	//if (lastDisplayedPosition != newPos)
		//displayPositionInfo(newPos);

	gainSlider.setValue(ourProcessor->gain, dontSendNotification);
	delaySlider.setValue(ourProcessor->delay, dontSendNotification);
}

// This is our Slider::Listener callback, when the user drags a slider.
void FilterAudioProcessorEditor::sliderValueChanged(Slider* slider)
{
	if (slider == &gainSlider)
	{
		// It's vital to use setParameterNotifyingHost to change any parameters that are automatable
		// by the host, rather than just modifying them directly, otherwise the host won't know
		// that they've changed.
		getProcessor()->setParameterNotifyingHost(FilterAudioProcessor::gainParam,
			(float)gainSlider.getValue());
	}
	else if (slider == &delaySlider)
	{
		getProcessor()->setParameterNotifyingHost(FilterAudioProcessor::delayParam,
			(float)delaySlider.getValue());
	}
}
