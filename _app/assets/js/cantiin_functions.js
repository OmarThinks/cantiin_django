function activateMainNavbarLink(linkname)
{
	let fullLinkName = "main_nav_link_" + linkname;
	document.getElementById(fullLinkName).classList.
	add('main_nav_link_active');

}