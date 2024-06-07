from plone.app.contenttypes.browser.collection import CollectionView
from plone.app.contenttypes.browser.folder import FolderView
from plone.dexterity.browser.view import DefaultView


class FolderGridListing(FolderView, DefaultView):
    pass


class CollectionGridListing(CollectionView, DefaultView):
    pass
