<?php

if ($view->getModule()->getIdentifier() == 'update') {
    $headerText = 'Update IAX modem';
} else {
    $headerText = 'Create a new IAX modem';
}

$mode = $view->fieldset()->setAttribute('template', $T('mode_label'))
            ->insert($view->radioButton('mode', 'both'))
            ->insert($view->radioButton('mode', 'send'))
            ->insert($view->radioButton('mode', 'receive'));

echo $view->panel()
    ->insert($view->header()->setAttribute('template', $T($headerText)))
    ->insert($view->textInput('name', ($view->getModule()->getIdentifier() == 'update' ? $view::STATE_READONLY : 0)))
    ->insert($view->textInput('server'))
    ->insert($view->textInput('extension'))
    ->insert($view->textInput('password', $view::TEXTINPUT_PASSWORD))
    ->insert($view->textInput('cidNumber'))
    ->insert($view->textInput('cidName'))
    ->insert($view->textInput('mail'))
    ->insert($mode);



echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL);
