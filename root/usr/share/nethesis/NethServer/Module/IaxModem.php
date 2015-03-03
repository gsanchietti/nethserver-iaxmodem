<?php
namespace NethServer\Module;

/*
 * Copyright (C) 2011 Nethesis S.r.l.
 * 
 * This script is part of NethServer.
 * 
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

use Nethgui\System\PlatformInterface as Validate;

/**
 * Manager IAX modems using modems db
 */
class IaxModem extends \Nethgui\Controller\TableController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Configuration', 20);
    }

    public function initialize()
    {
        $columns = array(
            'Key',
            'extension',
            'cidNumber',
            'mail',
            'Actions'
        );
        $modeValidator = $this->getPlatform()->createValidator()->memberOf(array('send','receive','both'));

        $parameterSchema = array(
            array('name', Validate::USERNAME, \Nethgui\Controller\Table\Modify::KEY),
            array('server', Validate::HOSTADDRESS, \Nethgui\Controller\Table\Modify::FIELD),
            array('extension', Validate::NOTEMPTY, \Nethgui\Controller\Table\Modify::FIELD),
            array('password', Validate::NOTEMPTY, \Nethgui\Controller\Table\Modify::FIELD),
            array('cidNumber', Validate::NOTEMPTY, \Nethgui\Controller\Table\Modify::FIELD),
            array('cidName', Validate::NOTEMPTY, \Nethgui\Controller\Table\Modify::FIELD),
            array('mail', Validate::EMAIL, \Nethgui\Controller\Table\Modify::FIELD),
            array('mode', $modeValidator, \Nethgui\Controller\Table\Modify::FIELD)
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('modems', 'iax'))
            ->setColumns($columns)
            ->addTableAction(new \Nethgui\Controller\Table\Modify('create', $parameterSchema, 'NethServer\Template\IaxModem\CreateUpdate'))            
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
            ->addRowAction(new \Nethgui\Controller\Table\Modify('update', $parameterSchema, 'NethServer\Template\IaxModem\CreateUpdate'))
            ->addRowAction(new \Nethgui\Controller\Table\Modify('delete', $parameterSchema, 'Nethgui\Template\Table\Delete'))
        ;

        parent::initialize();
    }

    public function bind(\Nethgui\Controller\RequestInterface $request)
    {
        $this->getAction('create')->setDefaultValue('mode','both');
        parent::bind($request);
    }


    public function prepareViewForColumnExtension(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        return $values['extension']."@".$values['server'];
    }

    public function prepareViewForColumnCidNumber(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        return $values['cidName']." (".$values['cidNumber'].")";
    }

    public function onParametersSaved(\Nethgui\Module\ModuleInterface $currentAction, $changes, $parameters)
    {
        $this->getPlatform()->signalEvent('nethserver-iaxmodem-save');
    }

}

