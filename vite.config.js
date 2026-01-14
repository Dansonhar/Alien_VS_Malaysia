import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    base: './',
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                alienCamp: resolve(__dirname, 'games/alien-camp.html'),
                alienCopycat: resolve(__dirname, 'games/alien-copycat.html'),
                baldiAirstrike: resolve(__dirname, 'games/baldi-airstrike.html'),
                coconutBowling: resolve(__dirname, 'games/coconut-bowling.html'),
                durianDodgeball: resolve(__dirname, 'games/durian-dodgeball.html'),
                laserBoss: resolve(__dirname, 'games/laser-boss.html'),
                slipperSniper: resolve(__dirname, 'games/slipper-sniper.html'),
                tehTarikToss: resolve(__dirname, 'games/teh-tarik-toss.html'),
                trafficJam: resolve(__dirname, 'games/traffic-jam.html'),
                ufoBasketball: resolve(__dirname, 'games/ufo-basketball.html'),
                whackAnAlien: resolve(__dirname, 'games/whack-an-alien.html'),
            },
        },
    },
});
