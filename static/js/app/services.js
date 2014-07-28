materialsApp.service('ApiService', function($http, $sce){

    this.getCategories = function(type){
        var url = getAPIUrl('categories/' + '?type=' + type);
        return $http.get(url).then(function(response){
            return response.data;
        });
    };

    this.getSubcategories = function(type, categoryId){
        var url = getAPIUrl('subcategories/' + '?type=' + type);
        if (categoryId) {
            url = url + '&category=' + categoryId;
        }
        return $http.get(url).then(function(response){
            return response.data;
        });
    };

    this.getDetail = function(detailId){
        var url = getAPIUrl('details/' + detailId + '/');
        return $http.get(url).then(function(response){
            var data = response.data;
            if (data.facts) {
                data.facts = $sce.trustAsHtml(data.facts);
            }
            if (data.video_url && data.video_url.indexOf('www.youtube.com/watch?v=') > 0){
                var url = data.video_url;
                data.code = data.video_url.substring(url.indexOf('www.youtube.com/watch?v=')+24);
            }
            return data;
        });
    };
});

materialsApp.service('SearchService', function($http){

    this.search = function(text){
        if (text.length < 3){
            return [];
        }
        var request = $http({
            url: getAPIUrl('search/'),
            method: 'GET',
            params: {'q': text}
        });
        return request.then(function(response){
            return response.data;
        });
    };
});