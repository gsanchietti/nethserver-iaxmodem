<?php

if ($view->getModule()->getIdentifier() == 'update') {
    $headerText = 'Update iaxmodem `${0}`';
} else {
    $headerText = 'Create a new iaxmodem';
}

echo $view->panel()
    ->insert($view->header('iaxmodem')->setAttribute('template', $headerText))
    ->insert($view->textInput('name', ($view->getModule()->getIdentifier() == 'update' ? $view::STATE_READONLY : 0)))
    ->insert($view->textInput('server'))
    ->insert($view->textInput('extension'))
    ->insert($view->textInput('password'))
    ->insert($view->textInput('cidNumber'))
    ->insert($view->textInput('cidName'));

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL);
