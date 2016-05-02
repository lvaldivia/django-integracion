Preload = function(game){}

Preload.prototype = {
    preload:function(){
        this.game.load.image('background',
            '/static/assets/background-texture.png');
        this.game.load.image('wall','/static/assets/wall.png');
        this.game.load.spritesheet('player','/static/assets/player.png',
            48, 48,4);
    },
    create:function(){
        this.game.state.start('Game');
    }
}