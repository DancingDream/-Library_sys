<template>
	<view class="container">
		<u-card :title="title" :sub-title="subTitle" :thumb="thumb" title-color="#000000">
			<view class="" slot="body">
				<view class="u-body-item-title u-line-2 status">已归还</view>
				<view class=""  style="margin-top: 10rpx;color: #999999;">
					<text>2022-03-15 23:19</text>
				</view>
				
			</view>
			<view class="" slot="foot">
				<u-icon name="hourglass"  size="28" label-color="#999999" color="" label="借书时间    2022-03-14 09:22"></u-icon>
			</view>
		</u-card>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: '红与黑',
				subTitle: '外国文学',
				thumb: '/static/img/bookMI.png',
			};
		}
	}
</script>

<style lang="scss">
	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
	}

	.u-body-item {
		font-size: 32rpx;
		// color: #333;
		padding: 20rpx 10rpx;
	}

	.u-body-item image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		border-radius: 8rpx;
		margin-left: 12rpx;
	}
	.status {
		font-weight: 700;
		font-size: 18px;
		color: #00aa7f;
	}
</style>
