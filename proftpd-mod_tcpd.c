/*
 * ProFTPD: mod_tcpd -- use TCPD library for access control
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307, USA.
 *
 * -- DO NOT MODIFY THE TWO LINES BELOW --
 * $Libraries: -lwrap$
 * $Id$
 *
 */

#include "conf.h"
#include "privs.h"
#include "tcpd.h"

#ifndef TCPD_ALLOW
int allow_severity = LOG_INFO;
int deny_severity = LOG_WARNING;
#endif
/*
 * -------------------------------------------------------------------------
 *   Configuration Handlers
 * -------------------------------------------------------------------------
 */

MODRET set_tcpd(cmd_rec * cmd)
{
	int b;

	CHECK_ARGS(cmd, 1);
	CHECK_CONF(cmd, CONF_ROOT | CONF_VIRTUAL | CONF_GLOBAL);

	if ((b = get_boolean(cmd, 1)) == -1)
		CONF_ERROR(cmd, "expected boolean argument.");

	add_config_param("UseTCPD", 1, (void *) b);

	return HANDLED(cmd);
}

MODRET set_tcpd_service(cmd_rec * cmd)
{
	char *service_name;

	CHECK_ARGS(cmd, 1);
	CHECK_CONF(cmd, CONF_ROOT | CONF_VIRTUAL | CONF_GLOBAL);

	service_name = cmd->argv[1];

	add_config_param_str("TCPDServiceName", 1, (void *) service_name);

	return HANDLED(cmd);
}

/*
 * These two functions are copied, almost verbatim, from the set_sysloglevel()
 * function in modules/mod_core.c.  I hereby cite the source for this code
 * as MacGuyver <macguyver@tos.net>. =)
 */

MODRET set_allow_syslog_level(cmd_rec * cmd)
{
	CHECK_ARGS(cmd, 1);
	CHECK_CONF(cmd, CONF_ROOT | CONF_VIRTUAL | CONF_ANON);

	if (!strcasecmp(cmd->argv[1], "emerg")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_EMERG);

	} else if (!strcasecmp(cmd->argv[1], "alert")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_ALERT);

	} else if (!strcasecmp(cmd->argv[1], "crit")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_CRIT);

	} else if (!strcasecmp(cmd->argv[1], "error")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_ERR);

	} else if (!strcasecmp(cmd->argv[1], "warn")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_WARNING);

	} else if (!strcasecmp(cmd->argv[1], "notice")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_NOTICE);

	} else if (!strcasecmp(cmd->argv[1], "info")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_INFO);

	} else if (!strcasecmp(cmd->argv[1], "debug")) {
		add_config_param("HostsAllowSyslogLevel", 1,
				 (void *) PR_LOG_DEBUG);

	} else {
		CONF_ERROR(cmd, "HostsAllowSyslogLevel requires level keyword: "
				"one of emerg/alert/crit/error/warn/notice/info/debug");
	}

	return HANDLED(cmd);
}

MODRET set_deny_syslog_level(cmd_rec * cmd)
{
	CHECK_ARGS(cmd, 1);
	CHECK_CONF(cmd, CONF_ROOT | CONF_VIRTUAL | CONF_ANON);

	if (!strcasecmp(cmd->argv[1], "emerg")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_EMERG);

	} else if (!strcasecmp(cmd->argv[1], "alert")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_ALERT);

	} else if (!strcasecmp(cmd->argv[1], "crit")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_CRIT);

	} else if (!strcasecmp(cmd->argv[1], "error")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_ERR);

	} else if (!strcasecmp(cmd->argv[1], "warn")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_WARNING);

	} else if (!strcasecmp(cmd->argv[1], "notice")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_NOTICE);

	} else if (!strcasecmp(cmd->argv[1], "info")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_INFO);

	} else if (!strcasecmp(cmd->argv[1], "debug")) {
		add_config_param("HostsDenySyslogLevel", 1,
				 (void *) PR_LOG_DEBUG);

	} else {
		CONF_ERROR(cmd, "HostsDenySyslogLevel requires level keyword: "
				"one of emerg/alert/crit/error/warn/notice/info/debug");
	}

	return HANDLED(cmd);
}

/*
 * -------------------------------------------------------------------------
 *  Command Handlers
 * -------------------------------------------------------------------------
 */

MODRET handle_request(cmd_rec * cmd)
{
	struct request_info request;
	char *service_name;

	/*
	 * If we haven't been explicitly disabled, enable us by default.
	 */
	if(get_param_int(TOPLEVEL_CONF, "UseTCPD", FALSE) == 0)
		return DECLINED(cmd);

	if ((allow_severity = get_param_int(CURRENT_CONF, "HostsAllowSyslogLevel",
					FALSE)) == -1)
		allow_severity = LOG_INFO;

	if ((deny_severity = get_param_int(CURRENT_CONF, "HostsDenySyslogLevel",
					FALSE)) == -1)
		deny_severity = LOG_WARNING;

	if ((service_name = (char *)get_param_ptr(CURRENT_CONF, "TCPDServiceName",
					FALSE)) == NULL)
		service_name = "proftpd";

	request_init(&request, RQ_DAEMON, service_name,
			RQ_FILE, session.c->rfd,
			RQ_CLIENT_SIN, session.c->remote_ipaddr,
			NULL);

	fromhost(&request);

	if (!hosts_access(&request)) {
		add_response_err(R_550,
				 "Unable to connect to %s: connection refused",
				 cmd->server->ServerFQDN);
		add_response_err(R_DUP,
				 "Please contact %s for more information",
				 cmd->server->ServerAdmin);
		refuse(&request);

		return ERROR(cmd);
	}

	/*
	 * if request is allowable, return DECLINED (for engine to act as if this
	 * handler was never called, else ERROR (for engine to abort processing and
	 * deny request.
	 */

	/* log the accepted connection */
#ifdef TCPD_ALLOW
	tcpd_allowlog(&request);
#else
	log_pri(priority, "connect from %s", eval_client(&request));
#endif

	return HANDLED(cmd);
}

static conftable tcpd_conftab[] = {
	{"HostsAllowSyslogLevel", set_allow_syslog_level, NULL},
	{"HostsDenySyslogLevel", set_deny_syslog_level, NULL},
	{"UseTCPD", set_tcpd, NULL},
	{"TCPDServiceName", set_tcpd_service, NULL},
	{NULL}
};

static cmdtable tcpd_cmdtab[] = {
	{PRE_CMD, C_PASS, G_NONE, handle_request, FALSE, FALSE},
	{0, NULL}
};

module tcpd_module = {
	NULL,
	NULL,
	0x20,
	"tcpd",
	tcpd_conftab,
	tcpd_cmdtab,
	NULL,
	NULL,
	NULL
};
