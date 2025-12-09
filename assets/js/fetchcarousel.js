fetch('carousel.html')
    .then(response => response.text())
    .then(data => {
        document.getElementById('carousel-placeholder').innerHTML = data;
        document.body.classList.remove('is-preload');
        
        // Initialize carousel after content is loaded
        initializeCarousel();
    })
    .catch(error => console.error('Error loading carousel:', error));

function initializeCarousel() {
    var settings = {
        carousels: {
            speed: 4,
            fadeIn: true,
            fadeDelay: 250
        }
    };

    $('.carousel').each(function() {

        var	$t = $(this),
            $forward = $('<span class="forward"></span>'),
            $backward = $('<span class="backward"></span>'),
            $reel = $t.children('.reel'),
            $items = $reel.children('article');

        // Clone items for infinite scroll
        var $clonedItems = $items.clone();
        $reel.append($clonedItems);

        var	pos = 0,
            leftLimit,
            rightLimit,
            itemWidth,
            reelWidth,
            originalReelWidth,
            timerId,
            autoScrollTimer;

        // Items.
        if (settings.carousels.fadeIn) {

            $items.addClass('loading');

            // Check if carousel is near top of page (for pages like NEWS)
            var carouselTop = $t.offset().top;
            var isNearTop = carouselTop < $(window).height();

            if (isNearTop) {
                // Immediately show items if carousel is at/near top
                var timerId,
                    limit = $items.length - Math.ceil($(window).width() / itemWidth);

                timerId = window.setInterval(function() {
                    var x = $items.filter('.loading'), xf = x.first();

                    if (x.length <= limit) {
                        window.clearInterval(timerId);
                        $items.removeClass('loading');
                        return;
                    }

                    xf.removeClass('loading');

                }, settings.carousels.fadeDelay);
            } else {
                // Use scrollex for carousels further down the page
                $t.scrollex({
                    mode: 'middle',
                    top: '-20vh',
                    bottom: '-20vh',
                    enter: function() {

                        var	timerId,
                            limit = $items.length - Math.ceil($(window).width() / itemWidth);

                        timerId = window.setInterval(function() {
                            var x = $items.filter('.loading'), xf = x.first();

                            if (x.length <= limit) {

                                window.clearInterval(timerId);
                                $items.removeClass('loading');
                                return;

                            }

                            xf.removeClass('loading');

                        }, settings.carousels.fadeDelay);

                    }
                });
            }

        }

        // Main.
        $t._update = function() {
            originalReelWidth = reelWidth / 2; // Half because we cloned items
            rightLimit = -originalReelWidth;
            leftLimit = 0;
            $t._updatePos();
        };

        $t._updatePos = function() { $reel.css('transform', 'translate(' + pos + 'px, 0)'); };

        // Auto-scroll function
        function startAutoScroll() {
            autoScrollTimer = window.setInterval(function() {
                pos -= settings.carousels.speed / 4;

                // Reset to start for seamless loop
                if (pos <= rightLimit) {
                    pos = leftLimit;
                }

                $t._updatePos();
            }, 50);
        }

        function stopAutoScroll() {
            if (autoScrollTimer) {
                window.clearInterval(autoScrollTimer);
            }
        }

        // Forward.
        $forward
            .appendTo($t)
            .hide()
            .mouseenter(function(e) {
                stopAutoScroll();
                timerId = window.setInterval(function() {
                    pos -= settings.carousels.speed;

                    if (pos <= rightLimit)
                    {
                        window.clearInterval(timerId);
                        pos = rightLimit;
                    }

                    $t._updatePos();
                }, 10);
            })
            .mouseleave(function(e) {
                window.clearInterval(timerId);
                startAutoScroll();
            });

        // Backward.
        $backward
            .appendTo($t)
            .hide()
            .mouseenter(function(e) {
                stopAutoScroll();
                timerId = window.setInterval(function() {
                    pos += settings.carousels.speed;

                    if (pos >= leftLimit) {

                        window.clearInterval(timerId);
                        pos = leftLimit;

                    }

                    $t._updatePos();
                }, 10);
            })
            .mouseleave(function(e) {
                window.clearInterval(timerId);
                startAutoScroll();
            });

        // Pause auto-scroll when hovering over carousel
        $t.mouseenter(function() {
            stopAutoScroll();
        }).mouseleave(function() {
            startAutoScroll();
        });

        // Init.
        $(window).on('load', function() {

            reelWidth = $reel[0].scrollWidth;

            if (breakpoints.active('<=medium')) {

                $reel
                    .css('overflow-y', 'hidden')
                    .css('overflow-x', 'scroll')
                    .scrollLeft(0);
                $forward.hide();
                $backward.hide();

            }
            else {

                $reel
                    .css('overflow', 'visible')
                    .scrollLeft(0);
                $forward.show();
                $backward.show();

            }

            $t._update();

            $(window).on('resize', function() {
                reelWidth = $reel[0].scrollWidth;
                $t._update();
            }).trigger('resize');

            // Start auto-scrolling
            startAutoScroll();

        });

        // If window is already loaded, trigger it immediately
        if (document.readyState === 'complete') {
            reelWidth = $reel[0].scrollWidth;

            if (breakpoints.active('<=medium')) {
                $reel
                    .css('overflow-y', 'hidden')
                    .css('overflow-x', 'scroll')
                    .scrollLeft(0);
                $forward.hide();
                $backward.hide();
            }
            else {
                $reel
                    .css('overflow', 'visible')
                    .scrollLeft(0);
                $forward.show();
                $backward.show();
            }

            $t._update();

            $(window).on('resize', function() {
                reelWidth = $reel[0].scrollWidth;
                $t._update();
            }).trigger('resize');

            // Start auto-scrolling
            startAutoScroll();
        }

    });
}

