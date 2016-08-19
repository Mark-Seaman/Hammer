angular.module('hammer', ['ui.bootstrap']);



function ThotCtrl($scope,$http) {
    $scope.showEdit = false
    $scope.showAdd = false
    $scope.showMove = false
    $scope.showRename = false
}


function BudgetController($scope) {
    $scope.name = 'Greeley Vineyard'

    $scope.income = 10000

    $scope.income_change = function() {
        $scope.giving         = parseInt($scope.income)*.1
        $scope.housing        = parseInt($scope.income)*.3
        $scope.groceries      = parseInt($scope.income)*.2
        $scope.healthcare     = parseInt($scope.income)*.1
        $scope.transportation = parseInt($scope.income)*.3
    }

    $scope.income_change()
}


var tabs = [
    { 'title':"Tab 1", 'content':'Text Body 1' },
    { 'title':"Tab 2", 'content':'Text Body 2' },
    { 'title':"Tab 3", 'content':'Text Body 3' }
]


function HammerCtrl($scope,$http) {

    $scope.text    = []
    $scope.id      = '42'
    $scope.child   = '0'
    $scope.xname   = 'New Name'
    $scope.gstatus = 'no status'
    $scope.gdata   = "no data"
    $scope.pstatus = 'no status'
    $scope.pdata   = "no data"

    $scope.get_name = function () {
        return $scope.xname
    }

    $scope.add_record = function (name) {
        var id = parseInt($scope.id)
        $scope.text.push( {"id": id, "name": name, "children": ""} )
        $scope.id = id+1
    }

    $scope.add_child = function (name,child) {
        $scope.text.push({"name": name, "children": child})
    }


    $scope.get_config_data = function () {
        $http.get('/get_thot')
        .success(function(data,status,headers,config) {
            $scope.gstatus = status
            $scope.gdata = data
            $scope.text = data  
        })
        .error (function(data,status,headers,config) { 
            $scope.gstatus = status // 'Error: failed to get_thot'
            $scope.gdata = data // "no data"
        })            
    }
    //$scope.get_config_data()


    $scope.put_config_data = function () {
        $http.post ('/put_thot', $scope.text)
            .success (function(data,status,headers,config) {
                $scope.pstatus = status // "Success status"
                $scope.pdata = data
            })
            .error (function(data,status,headers,config) { 
                $scope.pstatus = status //'Error: failed to put_thot'
                $scope.pdata = data //"no data"
            }) 
    }
    //$scope.put_config_data($scope.text)
}



function TabbedViewCtrl($scope) {
    $scope.tabs = tabs
}


function food_selector($scope) {

    $scope.selection = [ 'None' ]

    $scope.set_choices =  function(options) {
        $scope.options = options;
    }
        
    $scope.select_item = function(name) { 
        $scope.selection.push(name);
    }

    $scope.appetizers = '0'
}
