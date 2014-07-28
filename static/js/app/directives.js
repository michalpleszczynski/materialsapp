materialsApp.directive('socialMediaBar', function(){
    return {
        restrict: 'E',
        templateUrl: getPartialUrl('directives/social-media-bar.html'),
        controller: function(){
            // staticUrl is defined in base.html and is set to {% static '' %} from Django
            this.staticUrl = staticUrl;
        },
        controllerAs: 'socialMediaCtrl',
    };
});

materialsApp.directive('mainNavigation', function(){
    return {
        restrict: 'E',
        templateUrl: getPartialUrl('directives/main-navigation.html'),
        controller: function(){
            this.link = 0;

            this.selectLink = function(index) {
                this.link = index;
            };

            this.isSelected = function(index) {
                return this.link === index;
            };
        },
        controllerAs: 'navigationCtrl',
    };
});

materialsApp.directive('infoContactBar', function(){
    return {
        restrict: 'E',
        templateUrl: getPartialUrl('directives/info-contact-bar.html'),
        controller: function(){
            // staticUrl is defined in base.html and is set to {% static '' %} from Django
            this.staticUrl = staticUrl;
        },
        controllerAs: 'infoContactBarCtrl',
    };
});

materialsApp.directive('contactForm', function(){
    return {
        restrict: 'E',
        templateUrl: getPartialUrl('directives/contact-form.html'),
    };
});

materialsApp.directive('searchWidget', function(SearchService){
    return {
        restrict: 'E',
        scope: {},
        templateUrl: getPartialUrl('directives/search-widget.html'),
        link: function(scope, element, attrs){
            scope.text = '';

            scope.submit = function(){
                SearchService.search(scope.text).then(function(data){
                    scope.results = data.ans;
                });
            };
        }
    };
});

materialsApp.directive('youtube', function($sce) {
  return {
    restrict: 'EA',
    scope: { code:'=' },
    replace: true,
    template: '<div style="height:315px;"><iframe style="overflow:hidden;height:315px;width:560px" src="{{url}}" frameborder="0" allowfullscreen></iframe></div>',
    link: function (scope) {
        scope.$watch('code', function (newVal) {
           if (newVal) {
               scope.url = $sce.trustAsResourceUrl("http://www.youtube.com/embed/" + newVal);
           }
        });
    }
  };
});